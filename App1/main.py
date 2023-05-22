todos = []

while True:
    action = input("Type add[a], show[s], edit[e] or exit[x]:")

    match action:
        case 'add' | 'a':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show' | 's':
            for item in todos:
                print(item)
        case 'edit' | 'e':
            number = int(input("Option: "))
            new = input("New value: ")
            todos[number-1] = new
        case 'exit' | 'x':
            break

print("Bye")


