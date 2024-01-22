#!/usr/bin/python3
"""function that returns True if the object is an instance
of a class that inherited from the specified class; otherwise False"""


def inherits_from(obj, a_class):
    """checks if object returns True or False"""
    if type(obj) is a_class or not isinstance(obj, a_class):
        return False
    else:
        return isinstance(obj, a_class)
