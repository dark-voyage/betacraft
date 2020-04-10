import subprocess

memory = input("How many RAM you would like to allocate? e.g: 4000 (in megabytes)")

arguments = f"java -jar server.jar -Xms{memory}M -Xmx{memory}M"


def launching_server(argument):
    subprocess.call(argument)
    pass


if __name__ == '__main__':
    launching_server(arguments)
    pass
