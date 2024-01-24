#!/usr/bin/python3
"""a class Square that inherits from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class initialized"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """calculate area"""
        return (super().area())

    def __str__(self):
        """Magic method str"""
        return ("[Square] {}/{}".format(self.__size, self.__size))
