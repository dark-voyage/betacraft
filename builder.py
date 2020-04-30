import os
import shutil
import stat
import subprocess
import sys
import urllib.request


from glob import glob
from pathlib import Path


class Files:
    eula = \
        "eula=true"
    server_properties = "../assets/server/server.properties"
    server_icon = "../assets/server/server-icon.png"
    pass


builder_file = 'BuildTools.jar'
server = 'server'
directory = Path(__file__).resolve().parent
builds = 'builds'
url = "https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar"
version = "latest"  # input("Which version of Minecraft Server you would like to install: ")
messages = {
    "downloading": "Starting to download build tools!",
    "starting": "Starting to check everything before building.",
    "building": "Building stage is being started. Please, be patient!",
    "finishing": "Finishing building process.",
    "error": "Some error occurred!",
    "directory_created": f"The directory {builds} is created",
    "directory_exists": f"The directory {builds} already exists, re-creating it!",
    "renamed": "Server file has been successfully renamed and ready to be copied out!",
    "cleanup": "Cleaning up all used files and trashes!",
    "init": "Initializing the server with startup files...",
    "end": "This is the end of the program, thanks for your patience!",
}
# builder_arguments = f"java -jar BuildTools.jar"  # --rev {version}"
builder_arguments = [
    'java',
    '-jar',
    'BuildTools.jar'
]


def error(text):
    print("[ERROR] " + text)
    pass


def info(text):
    print("[INFO] " + text)
    pass


def success(text):
    print("[SUCCESS]" + text)
    pass


def builder():
    os.path.join(directory)

    try:
        os.mkdir(builds)
        success(messages["directory_created"])
        pass

    except FileExistsError:
        error(messages["directory_exists"])
        pass
    pass

    os.chdir(builds)
    info(messages["downloading"])
    try:
        urllib.request.urlretrieve(url, builder_file)
    except FileExistsError as err:
        os.remove(builder_file)
        urllib.request.urlretrieve(url, builder_file)
        pass

    info(messages["building"])
    subprocess.call(builder_arguments)

    for server_file in glob('spigot-*.*.*.jar'):
        info("Server version: " + server_file + " exists")
        try:
            os.rename(server_file, "server.jar")
        except FileExistsError as err:
            os.remove("server.jar")
            os.rename(server_file, "server.jar")
        success(messages["renamed"])
    pass

    os.chdir("..")
    print(directory)
    success(messages["finishing"])
    pass


def init():
    info(messages["init"])
    os.path.join(directory)

    try:
        os.mkdir(server)
        success(messages["directory_created"])

    except FileExistsError:
        error(messages["directory_exists"])
        shutil.rmtree(server)
        os.mkdir(server)
        success(messages["directory_created"])
    pass
    os.chdir(server)
    dst = str(directory) + "\\server"
    src = str(directory) + "\\builds"
    shutil.move(os.path.join(src, "server.jar"), os.path.join(dst, "server.jar"))

    with open("eula.txt", "w") as eula:
        eula.write(Files.eula)
        pass

    shutil.copy(Files.server_properties, ".")

    shutil.copy(Files.server_icon, ".")
    pass
    success(messages["end"])


def on_rm_error(path):
    os.chmod(path, stat.S_IWRITE)
    os.unlink(path)


def quit_builder():
    sys.stderr.write("[SUCCESS] " + "Beta Builder is exiting!")
    sys.exit(1)


if __name__ == '__main__':
    builder()
    init()
    quit_builder()
    pass
