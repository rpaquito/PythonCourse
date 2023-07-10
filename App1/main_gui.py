from modules import functions
import PySimpleGUI as Sg

label = Sg.Text("Type in a ToDo")
input_box = Sg.InputText(tooltip="Enter ToDo", key="todo")
add_button = Sg.Button("Add")
list_box = Sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=(45, 10))
edit_button = Sg.Button("Edit")


window = Sg.Window('My ToDo App',
                   layout=[
                       [label],
                       [input_box, add_button],
                       [list_box, edit_button]],
                   font=('Helvetica', 18))

while True:
    event, values = window.read()
    print(event)
    print(values)

    match event:
        case "Add":
            todos = functions.get_todos()
            todos.append(values['todo'] + "\n")
            functions.write_todos(todos)

            window["todos"].update(values=todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + "\n"
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case Sg.WINDOW_CLOSED:
            break

window.close()
