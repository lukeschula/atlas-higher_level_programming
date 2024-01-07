#!/usr/bin/python3

def uppercase(str):
    for x in str:
        char = ord(x)
        if char >= 97 and char <= 122:
            char -= 32
        print("{:c}".format(char), end='')
    print()
