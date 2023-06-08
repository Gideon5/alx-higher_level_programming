#!/usr/bin/python3
import sys

numArgs = len(sys.argv) - 1

if (numArgs == 0):
        print("{} arguments.".format(numArgs))
else:
    print("{} arguments:".format(numArgs))
    for i in range(numArgs):
        print("{}: {}".format(i+1, sys.argv[i+1]))
