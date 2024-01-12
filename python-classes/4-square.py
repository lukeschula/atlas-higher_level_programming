#!/usr/bin/python3
'''esatblishing Square class'''


class Square:
    '''creating a private attribute with the name size'''
    def __init__(self, size=0):
        @property
        def size(self):
            '''property to retrieve private instance'''
            return self.__size

        '''adding logic to ensure size must be an integer'''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        else:
            self.__size = size
            '''adding logic to ensure size is less than 0'''
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    '''creating a public instance called area to return area of the square'''
    def area(self):
        return self.__size * self.__size