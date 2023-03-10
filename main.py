from functions import *

while True:
    user_action = input("Type add, show, edit, complete or  exit: ")
    user_action = user_action.strip()
    if user_action.startswith('add'):
        todo = user_action[4:]
        todos = get_todos()
        todos.append(todo + '\n')
        write_todos(todos)

    elif user_action.startswith('show'):
        todos = get_todos()
        # new_todos = [item.strip('\n') for item in todos]
        # Try list comprehensions
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos = get_todos()
            todos[number] = new_todo + '\n'
            write_todos(todos)
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todos = get_todos()
            index = number - 1
            to_do_remove = todos[index].strip('\n')
            todos.pop(index)
            write_todos(todos)
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not Valid")

print("Bye")
