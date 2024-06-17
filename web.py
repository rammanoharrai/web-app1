import streamlit as st
import function
todos=function.get_todos()
def add_todo():
    todo=st.session_state["new_todo"]+'\n'
    todos.append(todo)
    function.write_todos(todos)

st.title('My Todo App')
st.subheader('This is my todo app')
st.write('to increase productivity')
todos=function.get_todos()
for index,todo in enumerate(todos):
    checkbox=st.checkbox(todo,key=index)
    if checkbox:
        todos.pop(index)
        function.write_todos(todos)
        del st.session_state[index]
        st.experimental_rerun()

st.text_input(label='Enter a new todo',
              placeholder="Write name of todo",on_change=add_todo,key="new_todo")

st.session_state
st