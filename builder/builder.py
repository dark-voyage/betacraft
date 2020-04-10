import subprocess
import wget
import shutil
import os

from pathlib import Path
from termcolor import colored

directory = Path(__file__).resolve().parent
dirname = 'builds'
url = "https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar"
version = input("Which version of Minecraft Server you would like to install: ")
messages = {
    "downloading": "Starting to download lab!",
    "starting": "Starting to check everything before building.",
    "building": "Building stage is being started. Please, be patient!",
    "finishing": "Finishing building process. Thanks for your patience!",
    "error": "Some error occurred!",
    "directory_created": f"The directory {dirname} is created",
    "directory_exists": f"The directory {dirname} already exists, re-creating it!",
}
builder_arguments = f'java -jar BuildTools.jar --rev {version}'


def error(text):
    print(colored(text, 'red', attrs=['bold']))
    pass


def info(text):
    print(colored(text, 'cyan', attrs=['bold']))
    pass


def success(text):
    print(colored(text, 'green', attrs=['bold']))
    pass


def check():
    os.path.join(directory)
    try:
        os.mkdir(dirname)
        success(messages["directory_created"])

    except FileExistsError:
        error(messages["directory_exists"])
        shutil.rmtree(dirname)
        os.mkdir(dirname)

    pass


def downloading(link):
    os.path.join(directory)
    os.chdir()
    info(messages["downloading"])
    wget.download(link)
    pass


def launching_builder(arguments):
    subprocess.call(arguments)
    pass


if __name__ == '__main__':
    check()
    downloading(url)
    launching_builder(builder_arguments)
    pass
