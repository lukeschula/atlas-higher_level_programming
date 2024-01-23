#!/usr/bin/python3
"""a function that reads a text file"""


def read_file(filename=""):
    """reads a text file, and prints it to stdout"""
    with open(filename, 'r', encoding='UTF8') as f:
        print(f.read())
