import os, sys
import subprocess
from pathlib import Path

launcher_arguments = [
    'java',
    '-jar',
    'server.jar',
]
message = {
    "start": "The Launcher is being started!",
    "process": "",
    "enter": "",
    "end": ""
}
directory = Path(__file__).resolve().parent


def error(text):
    print("[ERROR] " + text)
    pass


def info(text):
    print("[INFO] " + text)
    pass


def success(text):
    print("[SUCCESS]" + text)
    pass


def launching_server(argument):
    os.path.join(directory)
    os.chdir('server')
    subprocess.call(argument)
    pass


if __name__ == '__main__':
    launching_server(launcher_arguments)
    pass
