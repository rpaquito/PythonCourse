FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """
    Get the todos from the text file
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todolist, filepath=FILEPATH):
    """
    Write the todos into the text file
    """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todolist)


# Just executes if we run this file
if __name__ == "__main__":
    print(__name__)
    print("Functions imported")
