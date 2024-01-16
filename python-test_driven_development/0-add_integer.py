#!/usr/bin/python3
'''function that adds two integers'''


def add_integer(a, b=98):
    '''prototype with two integers, a and b must be an int or float,
    a and b must be first casted to integers if they are float,
     Returns an integer: the addition of a and b '''

    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')
    if type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
