import pip

packages = [
    'wget',
    'termcolor',
]


def setup():
    for package in packages:
        try:
            __import__(package)
        except ImportError:
            pip.main(['install', package])


setup()
