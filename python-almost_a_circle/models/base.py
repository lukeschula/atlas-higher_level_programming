#!/usr/bin/python3
""""almost a circle start"""



class Base:
    """writing the first class, Base"""
    def __init__(self, id=None):
        """class constructor"""
        self.id = id
        __nb_objects = 0

        if id != None:
            id =