from datetime import datetime
import configparser
import customtkinter
from PIL import Image
import os

def run_file(file_path):
    with open(file_path, 'r') as file:
        code = compile(file.read(), os.path.basename(file_path), 'exec')
    exec(code)

def write_file(logs_path, content):
    with open(logs_path, 'a') as file:
        file.write(content)

if __name__ == '__main__':
    logs_path = 'windows/cache/temps/logs.txt'
    content = f'{datetime.now()} : start {os.path.abspath(__file__)}\n'
    write_file(logs_path, content)

    file_path = 'windows/__init__.py'
    run_file(file_path)
