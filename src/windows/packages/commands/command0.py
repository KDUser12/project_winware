def display_commands():
    commands = [
        {
            'command': 'help',
            'description': 'Displays the list of commands.'
        },
        {
            'command': 'about',
            'description': 'Displays the program information.'
        }
    ]

    print('Commands:\n')
    for cmd in commands:
        print(f"- {cmd['command']} : {cmd['description']}")

if __name__ == '__main__':
    display_commands()
