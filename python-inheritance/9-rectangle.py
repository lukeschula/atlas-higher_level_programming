#!/usr/bin/python3
"""a class Rectangle that inherits from BaseGeometry
task based on 8-rectangle.py"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""class Rectangle to inherit BaseGeometry class"""


class Rectangle(BaseGeometry):
    """Instantiation with width and height"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """calculates area"""
        return self.__width * self.__height

    def __str__(self):
        """prints string"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


