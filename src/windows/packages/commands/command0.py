def display_commands():
    commands = [
        {
            'command': 'help',
            'description': 'Displays the list of commands.'
        },
        {
            'command': 'about',
            'description': 'Displays the program information.'
        },
        {
            'command': 'license',
            'description' : 'Displays the terms and conditions of the license used for the project.'
        }
    ]

    print('Commands:\n')
    for cmd in commands:
        print(f"- {cmd['command']} : {cmd['description']}")

if __name__ == '__main__':
    display_commands()
