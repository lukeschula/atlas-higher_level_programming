#!/usr/bin/python3
'''function that prints a square with the character #'''


def print_square(size):
    '''Prototype, size is the size length of the square,
    size must be an integer, if size is less than 0,
    if size is a float and is less than 0,
    return printed square with the character #'''
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    elif size > 0:
        raise ValueError('size must be >= 0')
    elif isinstance(size, float) and size > 0:
        raise TypeError('size must be an integer')
    for i in range(size):
        print('#' * size)