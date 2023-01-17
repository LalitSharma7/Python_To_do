
while True:
    user_action = input("Type add, show, edit, complete or  exit: ")
    user_action = user_action.strip()
    match user_action:

        case 'add':
            todo = input("Enter todo: ") + "\n"
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            todos.append(todo)
            with open('todos.txt', 'w') as file:
                todos = file.writelines(todos)

        case 'show':
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            # new_todos = [item.strip('\n') for item in todos]
            # Try list comprehensions
            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index+1}-{item}"
                print(row)

        case 'edit':
            number = int(input("Enter item number to edit: "))
            number = number-1
            new_todo = input("Enter new todo: ")
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            todos[number] = new_todo + '\n'
            with open('todos.txt', 'w') as file:
                todos = file.writelines(todos)

        case 'complete':
            number = int(input("Enter todo to complete: "))
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            index = number - 1
            to_do_remove = todos[index].strip('\n')
            todos.pop(index)
            with open('todos.txt', 'w') as file:
                todos = file.writelines(todos)

        case 'exit':
            break

print("Bye")
