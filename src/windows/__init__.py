from datetime import datetime

def write_to_file(file_path, content):
    with open(file_path, 'a') as file:
        file.write(content)

class Terminal:
    @staticmethod
    def commands_management(command):
        commands = ['help', 'about', 'start']
        
        if command not in commands:
            raise ValueError('Error code 1: The command you entered does not exist.')
        else:
            if command == commands[0]:
                with open('windows/packages/commands/command0.py', 'r') as file:
                    execute = compile(file.read(), 'command0.py', 'exec')
                    exec(execute)
            elif command == commands[1]:
                with open('windows/packages/commands/command1.py', 'r') as file:
                    execute = compile(file.read(), 'command1.py', 'exec')
                    exec(execute)

if __name__ == '__main__':
    print('''WinWARE - 1.0.0
Welcome to WinWare program control mode.
Here you can enter several commands, to know them enter help.
    ''')
    while True:
        command = input('> ')
       
        try:
            instance = Terminal()
            instance.commands_management(command)
        except ValueError as error:
            print(str(error))
            file_path = 'windows/cache/temps/logs.txt'
            content =  f'{datetime.now()} : command: {command}\n{datetime.now()} : result: {error}\n'
            write_to_file(file_path, content)
