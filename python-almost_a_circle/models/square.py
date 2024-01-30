#!/usr/bin/python3
"""Creating a Square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """Square class Constructor"""
        super().__init__(size, size, id, x, y)
