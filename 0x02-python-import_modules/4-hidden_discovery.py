#!/usr/bin/python3
import hidden_4


def printNames():
    for i in dir(hidden_4):
        if not (i.startswith('__')):
            print(i)


if __name__ == "__main__":
    printNames()
