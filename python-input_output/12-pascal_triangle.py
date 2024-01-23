#!/usr/bin/python3
"""returns a list of lists of integers representing the Pascals triangle"""


def pascal_triangle(n):
    """prototype"""
    if n <= 0:
        return []
    pas_tri = [[1 for column in range(row)] for row in range(1, n +1)]

    for x in range(2, n):
        for y in range(1, x):
            pas_tri[x][y] = pas_tri[x - 1][y] + pas_tri[x - 1][y - 1]
    return pas_tri
