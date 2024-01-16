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

    @property
    def position(self):
        '''get data'''
        return self.__position

    @position.setter
    def position(self, value):
        '''set position'''
        if not isinstance(value, tuple) or len(value) != 2 or \
        not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        '''return value'''
        self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        """sets size equal to 0, otherwise an empty line is printed"""
        if self.__size == 0:
            print("")
        else:
            '''prints in stdout the square with the character #'''
            for i in range(self.__size):
                print("#" * self.__size)