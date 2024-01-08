#!/usr/bin/python3
import sys

if __name__ != "__main__":
    exit()

    arg_tmp = "{:d} argument"
    argc = len(sys.argv) - 1
    if argc == 0:
        arg_tmp += 's.'
    elif argc == 1:
        arg_tmp += ':'
    else:
        arg_tmp += 's:'
    print(arg_tmp.forma
