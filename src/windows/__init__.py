from datetime import datetime
import os

def write_file(logs_path, content):
    with open(logs_path, 'a') as file:
        file.write(content)

def run_file(file_path):
    with open(file_path, 'r') as file:
        code = compile(file.read(), os.path.basename(file_path), 'exec')
    exec(code)

class Terminal:
    COMMANDS = {
        'help': 'windows/packages/commands/command0.py',
        'about': 'windows/packages/commands/command1.py',
        'credits': 'windows/packages/commands/command2.py',
        'start': 'windows/packages/window.py',
        'config': 'windows/packages/commands/command3.py',
        'admin': 'windows/packages/commands/command4.py'
    }

    @staticmethod
    def commands_management(command):
        if command not in Terminal.COMMANDS:
            raise ValueError('Error code 1: The command you entered does not exist.')

        file_path = Terminal.COMMANDS[command]
        if command == 'start' and not os.path.exists('windows/cache/temps/configuration.config'):
            raise ValueError('Error code 2: The configuration file was not found.')

        run_file(file_path)

        return 'The command is executed successfully!'

if __name__ == '__main__':
    logs_path = 'windows/cache/temps/logs.txt'

    print('''WinWARE - 1.0.0

Welcome to the WinWARE program control mode.
If you are new we advise you to enter the command "about" to learn more.
You can also enter the command "help" to know the list of commands.
          ''')
    while True:
        command = input('> ')
        try:
            result = Terminal.commands_management(command)
        except ValueError as error:
            print(error, '\n')
            result = error
        
        content = f'{datetime.now()} : Command: {command}\n{datetime.now()} : Result: {result}\n'
        write_file(logs_path, content)
