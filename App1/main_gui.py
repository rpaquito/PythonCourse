from modules import functions
import PySimpleGUI as Sg
import time

Sg.theme("DarkGreen1")

clock = Sg.Text("", key="clock")
label = Sg.Text("Type in a ToDo")
input_box = Sg.InputText(tooltip="Enter ToDo", key="todo")
add_button = Sg.Button("Add")
list_box = Sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=(45, 10))
edit_button = Sg.Button("Edit")
complete_button = Sg.Button("Complete")
exit_button = Sg.Button("Exit")

window = Sg.Window('My ToDo App',
                   layout=[
                       [label],
                       [clock],
                       [input_box, add_button],
                       [list_box, edit_button, complete_button],
                       [exit_button]],
                   font=('Helvetica', 18))

while True:
    event, values = window.read(timeout=1000)
    now = time.strftime("%b %d, %Y %H:%M:%S")
    window["clock"].update(value=now)

    match event:
        case "Add":
            todos = functions.get_todos()
            todos.append(values['todo'] + "\n")
            functions.write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value="")
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + "\n"
                functions.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                Sg.popup("Please select an item first")
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                Sg.popup("Please select an item first")
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case "Exit":
            break
        case Sg.WINDOW_CLOSED:
            break

window.close()
