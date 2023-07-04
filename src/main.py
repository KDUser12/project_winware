from datetime import datetime
import os

def write_to_file(content, file_path):
    with open(file_path, 'a') as file:
        file.write(str(content))

def start_file():
    with open('windows/__init__.py', 'r') as file:
        execute = compile(file.read(), '__init__.py', 'exec')
        exec(execute)

if __name__ == '__main__':
    file_path = 'windows/cache/temps/logs.txt'
    content = f'{datetime.now()} : start {os.path.abspath(__file__)}\n'
    write_to_file(content, file_path)
    start_file()
