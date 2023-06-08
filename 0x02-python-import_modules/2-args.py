#!/usr/bin/python3
import sys


def printNums():
    numArgs = len(sys.argv) - 1

    if (numArgs == 0):
        print("{} arguments.".format(numArgs))
    else:
        print("{} arguments:".format(numArgs))
        for i in range(numArgs):
            print("{}: {}".format(i+1, sys.argv[i+1]))




if __name__ == "__main__":
    printNums()
