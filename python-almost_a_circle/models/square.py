#!/usr/bin/python3
"""Creating a Square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """Square class Constructor"""
        super().__init__(size, size, id, x, y)

    def __str__(self):
        """overloading __str__ method should return
        [Square] (<id>) <x>/<y> - <size>"""
        return ("[Square] ({}) {}/{} - {}").format(id, self.x, self.y, self.width, self.height)
