
FilePath = r"C:\Users\lalisharma\Documents\ToDo\todos.txt"


def get_todos(filepath=FilePath):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FilePath):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print(get_todos())