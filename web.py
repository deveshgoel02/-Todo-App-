import streamlit as st
import functions
from datetime import date,time

st.markdown(
    """
    <style>
    /* Full gradient background */
    .stApp {
        background: linear-gradient(135deg, #667eea, #764ba2);
        font-family: 'Segoe UI', sans-serif;
    }

    /* Main container card */
    section.main > div {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(12px);
        padding: 2rem;
        border-radius: 20px;
        max-width: 700px;
        margin: auto;
        box-shadow: 0 15px 35px rgba(0,0,0,0.2);
    }

    /* Title */
    h1 {
        text-align: center;
        color: white;
        font-weight: 700;
    }

    /* Subtitle text */
    h3, p {
        text-align: center;
        color: #f1f1f1;
    }

    /* Todo text */
    label {
        color: white !important;
        font-size: 18px;
    }

    /* Checkbox spacing */
    div[data-testid="stCheckbox"] {
        margin-bottom: 12px;
    }
    
    div.stButton > button {
    background-color: black;
    color: white;
    border-radius: 10px;
    border: none;
}


    /* Input box */
    input {
        border-radius: 12px !important;
        padding: 12px !important;
        font-size: 16px !important;
    }

    /* Remove Streamlit footer */
    footer {
        visibility: hidden;
    }
    </style>
    """,
    unsafe_allow_html=True
)

todos = functions.get_todos()

def add_todo():
    task = st.session_state["task"]
    due_date = st.session_state["due_date"]
    due_time = st.session_state["due_time"]

    formatted_time = due_time.strftime("%I:%M %p").lstrip("0").lower()
    formatted_date = due_date.strftime("%d/%m/%Y")

    todo = f"{task} | {formatted_time} || {formatted_date}\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("📝 Todo App with Due Dates")
st.subheader("Stay organized. Stay productive.")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):

    parts = todo.strip().split(" | ", 1)
    task = parts[0]

    time_date = parts[1] if len(parts) == 2 else ""

    if "||" in time_date:
        time_part, date_part = time_date.split("||")
    else:
        time_part, date_part = "", ""

    col1, col2 = st.columns([4, 1])

    with col1:
        checked = st.checkbox(task, key=f"todo_{index}")

    with col2:
        st.markdown(
            f"""
            <div style="text-align:right; color:white;">
                <div style="font-weight:600;">{time_part.strip()}</div>
                <div style="font-size:14px; opacity:0.8;">{date_part.strip()}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    if checked:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[f"todo_{index}"]
        st.rerun()


st.text_input(
    label="",
    placeholder="Add a new todo...",
    key="task"
)
st.time_input(
    label="Time",
    key="due_time"
)

st.date_input(
    label="Due date",
    min_value=date.today(),
    key="due_date"
)

st.button("Add Task", on_click=add_todo)



