import subprocess

memory = input("How many RAM you would like to allocate? e.g: 4000 (in megabytes)")

arguments = [
    'java',
    '-jar',
    'server.jar',
    f'-Xms{memory}M',
    f'-Xmx{memory}M'
]


def launching_server(file):
    subprocess.call(arguments)
    pass


