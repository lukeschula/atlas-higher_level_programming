#!/usr/bin/python3
"""a function that writes a string to a text file"""


def write_file(filename="", text=""):
    """"writes a string to a text file,
    and returns the number of characters written"""

    with open(filename, encoding="uft-8") as f:
        file = open('my_first_file.txt', 'w')
        file.write("This School is so cool!\n")
