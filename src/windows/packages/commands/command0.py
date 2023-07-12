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
            'command': 'credits',
            'description': 'Displaying the full list of software developers.'
        },
        {
            'command': 'start',
            'description': 'Launch the WinWARE application.'
        },
        {
            'command': 'config',
            'description': 'WinWARE application configuration.'
        }
    ]

    print('\nCommands:\n')
    for cmd in commands:
        print(f"- {cmd['command']} : {cmd['description']}")
    print('')

if __name__ == '__main__':
    display_commands()
