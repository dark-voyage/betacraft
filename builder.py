import subprocess
import urllib.request
import shutil
import os
from glob import glob
from pathlib import Path


class Colors:
    CEND = '\33[0m'
    CBOLD = '\33[1m'
    CITALIC = '\33[3m'
    CURL = '\33[4m'
    CBLINK = '\33[5m'
    CBLINK2 = '\33[6m'
    CSELECTED = '\33[7m'
    ####################
    CBLACK = '\33[30m'
    CRED = '\33[31m'
    CGREEN = '\33[32m'
    CYELLOW = '\33[33m'
    CBLUE = '\33[34m'
    CVIOLET = '\33[35m'
    CBEIGE = '\33[36m'
    CWHITE = '\33[37m'
    ####################
    CBLACKBG = '\33[40m'
    CREDBG = '\33[41m'
    CGREENBG = '\33[42m'
    CYELLOWBG = '\33[43m'
    CBLUEBG = '\33[44m'
    CVIOLETBG = '\33[45m'
    CBEIGEBG = '\33[46m'
    CWHITEBG = '\33[47m'

    CGREY = '\33[90m'
    CRED2 = '\33[91m'
    CGREEN2 = '\33[92m'
    CYELLOW2 = '\33[93m'
    CBLUE2 = '\33[94m'
    CVIOLET2 = '\33[95m'
    CBEIGE2 = '\33[96m'
    CWHITE2 = '\33[97m'
    ####################
    CGREYBG = '\33[100m'
    CREDBG2 = '\33[101m'
    CGREENBG2 = '\33[102m'
    CYELLOWBG2 = '\33[103m'
    CBLUEBG2 = '\33[104m'
    CVIOLETBG2 = '\33[105m'
    CBEIGEBG2 = '\33[106m'
    CWHITEBG2 = '\33[107m'

    pass


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
    server_icon = "../assets/server/server-icon.png"
    pass


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
    print(Colors.CRED + Colors.CBOLD + text + Colors.CEND)
    pass


def info(text):
    print(Colors.CBLUE2 + Colors.CBOLD + text + Colors.CEND)
    pass


def success(text):
    print(Colors.CGREEN + Colors.CBOLD + text + Colors.CEND)
    pass


def builder():
    os.path.join(directory)

    try:
        os.mkdir(builds)
        success(messages["directory_created"])

    except FileExistsError:
        error(messages["directory_exists"])
        shutil.rmtree(builds)
        os.mkdir(builds)
        success(messages["directory_created"])

    os.chdir(builds)
    info(messages["downloading"])
    urllib.request.urlretrieve(url, 'BuildTools.jar')

    info(messages["building"])
    subprocess.call(builder_arguments)

    for server_file in glob('spigot-*.*.*.jar'):
        info("Server version: " + server_file + " exists")
        os.rename(server_file, "server.jar")
        src = os.getcwd()
        dst = Path(__file__).resolve().parent
        shutil.move(os.path.join(src, "server.jar"), os.path.join(dst, "server.jar"))
        success(messages["moved"])
    pass

    os.chdir("..")
    shutil.rmtree(builds)
    info(messages["cleanup"])

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
    dst = os.getcwd()
    src = Path(__file__).resolve().parent
    shutil.move(os.path.join(src, "server.jar"), os.path.join(dst, "server.jar"))

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
