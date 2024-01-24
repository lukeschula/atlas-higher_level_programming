#!/usr/bin/python3
"""a class Square that inherits from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class initialized"""
    def __init__(self, size):
        self.__size = self.integer_validator("size", size)

        super().__init__(size, size)
