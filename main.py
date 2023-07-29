import streamlit as st
import functions

todo_list = functions.get_todos("todos.txt")


def add_new_todo():
    todo_value = st.session_state["new_todo"]
    todo_list.append(todo_value+"\n")
    functions.write_todos(todo_list)


st.title("My Todo App")

for index, todo in enumerate(todo_list):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todo_list.pop(index)
        functions.write_todos(todo_list)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Add Todo", label_visibility="hidden",
              placeholder="Add your new Todo Here", key="new_todo",
              on_change=add_new_todo)
