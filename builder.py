import subprocess
import wget
import shutil
import os
import files

from glob import glob
from pathlib import Path
from termcolor import colored

class Files:
    eula = \
        "eula=true"

    server_properties = \
        """spawn-protection=16
    max-tick-time=60000
    query.port=25565
    generator-settings=
    force-gamemode=false
    allow-nether=true
    enforce-whitelist=false
    gamemode=survival
    broadcast-console-to-ops=true
    enable-query=false
    player-idle-timeout=0
    difficulty=easy
    spawn-monsters=true
    broadcast-rcon-to-ops=true
    op-permission-level=4
    pvp=true
    snooper-enabled=true
    level-type=default
    hardcore=false
    enable-command-block=true
    max-players=100
    network-compression-threshold=256
    resource-pack-sha1=
    max-world-size=29999984
    function-permission-level=2
    rcon.port=25575
    server-port=25565
    debug=false
    server-ip=127.0.0.1
    spawn-npcs=true
    allow-flight=true
    level-name=beta_world
    view-distance=10
    resource-pack=
    spawn-animals=true
    white-list=false
    rcon.password=mogulkahn2001
    generate-structures=true
    max-build-height=256
    online-mode=false
    level-seed=
    use-native-transport=true
    prevent-proxy-connections=false
    motd=\u00A7a\u1360\u00A72 Welcome to\u00A7c BetaCraft \u00A72Server\u00A79       t.me/bsba_group\u00A7r\n\u00A7a\u1360\u00A7e Start playing in our Server\!\!\!
    enable-rcon=false
    """

    server_icon = "assets/server/server-icon.png"
    pass


directory = Path(__file__).resolve().parent
dirname = 'builds'
url = "https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar"
version = "latest"  # input("Which version of Minecraft Server you would like to install: ")
messages = {
    "downloading": "Starting to download build tools!",
    "starting": "Starting to check everything before building.",
    "building": "Building stage is being started. Please, be patient!",
    "finishing": "Finishing building process.",
    "error": "Some error occurred!",
    "directory_created": f"The directory {dirname} is created",
    "directory_exists": f"The directory {dirname} already exists, re-creating it!",
    "moved": "Server file has been successfully moved to parent directory!",
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
    print(colored(text, 'red', attrs=['bold']))
    pass


def info(text):
    print(colored(text, 'cyan', attrs=['bold']))
    pass


def success(text):
    print(colored(text, 'green', attrs=['bold']))
    pass


def builder():
    os.path.join(directory)

    try:
        os.mkdir(dirname)
        success(messages["directory_created"])

    except FileExistsError:
        error(messages["directory_exists"])
        shutil.rmtree(dirname)
        os.mkdir(dirname)
        success(messages["directory_created"])

    os.chdir(dirname)
    info(messages["downloading"])
    wget.download(url)

    info(messages["building"])
    subprocess.call(builder_arguments)

    for server_file in glob('spigot-*.*.*.jar'):
        info("Server version: " + server_file + " exists")
        os.rename(server_file, "builder/server.jar")
        shutil.move("builder/server.jar", Path(__file__).resolve().parent)
        success(messages["moved"])
    pass

    shutil.rmtree(dirname)
    info(messages["cleanup"])

    success(messages["finishing"])
    pass


def init():
    info(messages["init"])
    with open("eula.txt", "w") as eula:
        eula.write(Files.eula)
        pass

    with open("server.properties", "w") as properties:
        properties.write(Files.server_properties)
        pass

    shutil.copy(Files.server_icon, ".")
    pass
    success(messages["end"])


if __name__ == '__main__':
    builder()
    init()
    exit(1)
    pass
