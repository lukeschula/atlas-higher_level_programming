#!/usr/bin/python3
"""creating Rectangle class that inherits from Base"""

Base = __import__('base')

class Rectangle(Base):
    """Rectangle class, adding
    Private instance attributes
    and class constructor"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
