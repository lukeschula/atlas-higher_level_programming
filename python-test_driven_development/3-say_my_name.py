#!/usr/bin/python3
'''a function that prints My name is <first name> <last name>'''


def say_my_name(first_name, last_name=""):
    '''Prototype, first_name and last_name must be strings,
    returns the first and lat name'''
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    return print("My name is {} {}".foramt(first_name, last_name))

