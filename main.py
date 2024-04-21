from functions import (
    add_todo,
    complete_todo,
    edit_todo,
    get_todos,
    show_todos,
)


COMMANDS = {
    'add': add_todo,
    'show': show_todos,
    'edit': edit_todo,
    'complete': complete_todo,
    'exit': None,
}


def get_command_and_text():
    user_input = input("Type add, show, edit, complete or exit: ")
    input_words = user_input.split()
    user_action = input_words[0]
    user_data = ''
    if len(input_words) > 1:
        user_data = ' '.join(input_words[1:])
    return user_action, user_data


def run_terminal_application():
    while True:
        command, text = get_command_and_text()

        if command not in COMMANDS:
            print('Command is not Valid')
            continue

        if command == 'exit':
            print('Bye')
            break

        all_todos = get_todos()
        action_function = COMMANDS[command]
        action_function(all_todos, text)


if __name__ == '__main__':
    run_terminal_application()
