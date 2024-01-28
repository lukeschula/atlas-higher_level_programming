#!/usr/bin/python3
""""almost a circle start"""


__nb_objects = 0

class Base:
    """writing the first class, Base"""
    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects