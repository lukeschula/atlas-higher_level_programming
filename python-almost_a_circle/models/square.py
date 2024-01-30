#!/usr/bin/python3
"""Creating a Square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Square class Constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.height

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """overloading __str__ method should return
        [Square] (<id>) <x>/<y> - <size>"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                  self.y, self.width))
