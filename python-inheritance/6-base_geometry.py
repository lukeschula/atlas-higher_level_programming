#!/usr/bin/python3
"""class BaseGeometry, based on 5-base_geometry.py"""


class BaseGeometry:
    """adding public instance method, that raises an Exception"""
    def area(self):
        Exception("area() is not implemented")
