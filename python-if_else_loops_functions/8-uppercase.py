#!/usr/bin/python3

def uppercase(str):
    for x in range(len(str)):
        char = ord(str[x])
        if char >= 97 and char <= 122:
            char = char - 32
        print("{}".format(chr(char)), end='')
        print()

