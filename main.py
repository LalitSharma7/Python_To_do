
todos = []
while True:
    user_action = input("Type add, show, edit, complete or  exit: ")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input("Enter todo: ")
            todos.append(todo)
        case 'show':
            for index, item in enumerate(todos):
                row = f"{index+1}-{item}"
                print(row)
        case 'edit':
            number = int(input("Enter item number to edit: "))
            number = number-1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case 'complete':
            number = int(input("Enter todo to complete: "))
            todos.pop(number-1)
        case 'exit':
            break

print("Bye")
