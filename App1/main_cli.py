# from functions import get_todos, write_todos
from modules import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    action = input("Type add, show, edit, complete or exit:")
    action = action.strip()

    if action.startswith('add'):
        todo = action[4:] + "\n"

        todos = functions.get_todos()
        todos.append(todo)

        functions.write_todos(todos)

    elif action.startswith('show'):
        todos = functions.get_todos()

        # list comprehensions example
        # new_todos =[item.strip("\n") for item in todos]

        for index, item in enumerate(todos):
            row = f"{index + 1} - {item}"
            print(row.strip("\n"))

    elif action.startswith('edit'):
        try:
            number = int(action[5:])
            todos = functions.get_todos()

            new = input("New value: ")
            todos[number - 1] = new + "\n"

            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid")
            continue

    elif action.startswith('complete'):
        try:
            todos = functions.get_todos()

            number = int(action[9:])
            todo_to_remove = todos[number - 1].strip("\n")
            todos.pop(number - 1)

            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("Item doesn't exist.")
            continue

    elif action.startswith('exit'):
        break
    else:
        print("Command not valid.")

print("Bye")
