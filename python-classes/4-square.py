#!/usr/bin/python3
'''esatblishing Square class'''


class Square:
    '''creating a private attribute with the name size'''
    def __init__(self, size=0):
        self.size = size
    @property
    def size(self):
        '''property to retrieve private instance attribute'''
        return self.__size

    @size.setter
    def size(self, value):
        '''adding logic to ensure size must be an integer'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        '''adding logic to ensure size is less than 0'''
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    '''creating a public instance called area to return area of the square'''
    def area(self):
        return self.__size * self.__size