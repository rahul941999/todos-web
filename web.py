import streamlit as st
import functions


todos = functions.read()


def add_todo():
    todo_local = st.session_state["new_todo"]
    todos.append(todo_local + "\n")
    st.session_state['new_todo'] = ""
    functions.write(todos)


st.title("My Todo App")
st.subheader("This is todo app")
st.write("This app helps to keep trak of things that you need to do.")

for index, todo in enumerate(todos):
    chkbx = st.checkbox(todo, key=todo)
    if chkbx:
        todos.pop(index)
        functions.write(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter a todo :", placeholder="Add a new todo..",
              label_visibility="hidden", on_change=add_todo, key="new_todo")
