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
    @staticmethod
    def commands_management(command):
        commands = ['help', 'about', 'credits', 'start', 'config', 'admin']

        if command not in commands:
            raise ValueError('Error code 1: The command you entered does not exist.')
        
        if command == commands[0]:
            file_path = 'windows/packages/commands/command0.py'
        elif command == commands[1]:
            file_path = 'windows/packages/commands/command1.py'
        elif command == commands[2]:
            file_path = 'windows/packages/commands/command2.py'
        elif command == commands[3]:
            if os.path.exists('windows/cache/temps/configuration.config'):
                file_path = 'windows/packages/window.py'
            else: 
                raise ValueError('Error code 2: The configuration file was not found.')
        elif command == commands[4]:
            file_path = 'windows/packages/commands/command3.py'
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