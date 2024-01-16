#!/usr/bin/python3
'''an empty class Rectangle'''

class Rectangle:
    '''creates a class than defines a rectangle'''
    def __init__(self, width=0, height=0):
        '''attributes of a rectangle'''
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__width = width
        self.__height = height

    @property
    def height(self):
        '''retrieve data'''
        return self.__height

    @height.setter
    def height(self, value):
        '''setter to set height'''
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
            self.__height = value

    @property
    def width(self):
        '''retrieve data'''
        return self.__width

    @height.setter
    def width(self, value):
        '''setter to set width'''
        if type(value) is not int:
            raise TypeError('width must be an integer')
            self.__width = value

    def area(self):
        '''finds area of rectangle'''
        return self.__width * self.__height

    def perimeter(self):
        '''finds perimater of rectangle'''
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

