import streamlit as st
import functions

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
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)




st.title('My Todo App')
st.subheader('This is my Todo App')
st.write("This app is to increase your productivity")

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Add a new todo...",
              on_change=add_todo,key="new_todo")



