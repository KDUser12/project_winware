from datetime import datetime
from typing import Self
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
    def commands_management(self, command):
        commands = ['help', 'about', 'start']

        if command not in commands:
            result = ValueError('Error code 1: The command you entered does not exist')
            return result
        else:
            if command == commands[0]:
                file_path = 'windows/packages/commands/command0.py'
            elif command == commands[1]:
                file_path = 'windows/packages/commands/command1.py'
            elif command == commands[2]:
                file_path = 'windows/packages/windows.py'
            run_file(file_path)

            result = 'The command is executed successfully!'
            return result

if __name__ == '__main__':
    print('''WinWARE - 1.0.0

Bienvenue dans le mode commande du programme WinWARE.
Si vous êtes nouveau nous vous conseillons d'entrer la commande "about" pour en savoir plus.

          
          ''')
    while True:
        command = input('> ')
        result = Terminal.commands_management(Self, command)
        print(result)

        logs_path = 'windows/cache/temps/logs.txt'
        content = f'{datetime.now()} : Command: {command}\n{datetime.now()} : Result: {result}\n'
        write_file(logs_path, content)















