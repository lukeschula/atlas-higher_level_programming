#!/usr/bin/python3
'''function that divides all elements of a matrix'''

def matrix_divided(matrix, div):
    '''prototype to function,matrix must be a list of lists of integers or floats,
    Each row of the matrix must be of the same size,div must be a number
    div cannott be equal to 0, All elements of the matrix should be divided by div
    Returns a new matrix'''

    if type(matrix) is not list or matrix == [] is None:
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    if not all(isinstance(x, list) for x in matrix):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    if not all(len(l) == len(matrix[0]) for l in matrix):
        raise TypeError('Each row of the matrix must have the same size')
    for lists in matrix:
        if not all(isinstance(elements, (int, float)) for elements in lists):
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    new_list = [[round(elements / div, 2) for elements in lists] for lists in matrix]
    return new_list