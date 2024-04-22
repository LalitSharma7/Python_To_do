from pathlib import Path


FILE_FOLDER = Path('.')
FILE_NAME = 'todos.txt'
FILE_PATH = FILE_FOLDER / FILE_NAME


def get_todos(filepath=FILE_PATH):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILE_PATH):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


def add_todo(todos, todo_description):
    todos.append(todo_description + '\n')
    write_todos(todos)


def show_todos(todos, todo_description):
    for index, item in enumerate(todos, 1):
        item = item.strip('\n')
        print(f'{index} - {item}')


def edit_todo(todos, todo_description):
    try:
        number = int(todo_description) - 1
        previous_todo = todos[number]
    except ValueError:
        print('Your command is not valid.')
        return
    except IndexError:
        print('There is no item with that number.')
        return

    new_todo = input('Enter new todo: ')
    todos[number] = f'{new_todo}\n'
    write_todos(todos)


def complete_todo(todos, todo_description):
    todo_index = int(todo_description) - 1

    try:
        todos.pop(todo_index)
    except IndexError:
        print('There is no item with that number.')
        return

    write_todos(todos)


if __name__ == "__main__":
    print(get_todos())
