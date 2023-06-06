def get_todos():
    with open('files/todos.txt', 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


while True:
    action = input("Type add, show, edit, complete or exit:")
    action = action.strip()

    if action.startswith('add'):
        todo = action[4:] + "\n"

        todos = get_todos()
        todos.append(todo)

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)

    elif action.startswith('show'):
        todos = get_todos()

        # list comprehensions example
        # new_todos =[item.strip("\n") for item in todos]

        for index, item in enumerate(todos):
            row = f"{index + 1} - {item}"
            print(row.strip("\n"))

    elif action.startswith('edit'):
        try:
            number = int(action[5:])
            todos = get_todos()

            new = input("New value: ")
            todos[number - 1] = new + "\n"

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not valid")
            continue

    elif action.startswith('complete'):
        try:
            todos = get_todos()

            number = int(action[9:])
            todo_to_remove = todos[number - 1].strip("\n")
            todos.pop(number - 1)

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)

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
