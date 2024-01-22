#!/usr/bin/python3
"""a class Rectangle that inherits from BaseGeometry"""


class Rectangle(BaseGeometry):
    """Instantiation with width and height"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
