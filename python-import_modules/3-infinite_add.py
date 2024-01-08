#!/usr/bin/python3

from sys import argv
if __name__ == "__main__":
    countr = len(argv)
    add = 0
    if countr == 1:
        print("{}".format(add))
    else:
        for i in range(1, countr):
            add += int(argv.__getitem__(i))
        print("{}".format(add))

