#!/usr/bin/python3
'''esatblishing Square class'''


class Square:
    '''creating a private attribute with the name size'''
    def __init__(self,size=0):
        '''adding logic to ensure size must be an integer'''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        else:
            self.__size = size 