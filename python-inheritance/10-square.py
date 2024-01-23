#!/usr/bin/python3
"""a class Square that inherits from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle
"""class Square to inherit Rectangle class"""


class Square(Rectangle):
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)

        super().__init__(size, size)
