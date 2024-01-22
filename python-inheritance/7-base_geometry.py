#!/usr/bin/python3
"""class BaseGeometry, 6-base_geometry.py"""


class BaseGeometry:
    """adding public instance method, that raises an Exception"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if value is not int:
            raise TypeError("name must be an integer")
        if value <= 0:
            raise ValueError("name must be greater than 0")
