from modules import functions
import PySimpleGUI as Sg

label = Sg.Text("Type in a ToDo")
input_box = Sg.InputText(tooltip="Enter ToDo")
add_button = Sg.Button("Add")

window = Sg.Window('My ToDo App', layout=[[label], [input_box, add_button]])
window.read()
print("Hello from inside")
window.close()
