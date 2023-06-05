while True:
    action = input("Type add, show, edit, complete or exit:")

    if 'add' in action:
        todo = action[4:] + "\n"

        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo)

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'show' in action:
        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        # list comprehensions example
        # new_todos =[item.strip("\n") for item in todos]

        for index, item in enumerate(todos):
            row = f"{index + 1} - {item}"
            print(row.strip("\n"))

    elif 'edit' in action:
        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        number = int(action[5:])
        new = input("New value: ")
        todos[number - 1] = new + "\n"

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'complete' in action:
        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        number = int(action[9:])
        todo_to_remove = todos[number - 1].strip("\ns")
        todos.pop(number - 1)

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)

        message = f"Todo {todo_to_remove} was removed from the list."
        print(message)

    elif 'exit' in action:
        break
    else:
        print("Command not valid.")

print("Bye")

