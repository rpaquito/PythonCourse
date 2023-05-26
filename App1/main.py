todos = []

while True:
    action = input("Type add[a], show[s], edit[e], complete[c] or exit[x]:")

    match action:
        case 'add' | 'a':
            todo = input("Enter a todo: ")
            todos.append(todo)

        case 'show' | 's':
            for index, item in enumerate(todos):
                row = f"{index + 1} - {item}"
                print(row)
        case 'edit' | 'e':
            number = int(input("Option: "))
            new = input("New value: ")
            todos[number - 1] = new
        case 'complete' | 'c':
            number = int(input("Option: "))
            todos.pop(number - 1)
        case 'exit' | 'x':
            break

print("Bye")


