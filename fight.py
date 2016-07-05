# /usr/bin/python3

# MELNIKOV ILYA

from factory import *


def main():
    factory = Factory()
    battlefield = factory.create_battlefield()
    battlefield.start()


if __name__ == '__main__':
    main()
