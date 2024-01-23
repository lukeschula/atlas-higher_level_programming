#!/usr/bin/python3
"""Write a class Student that defines a student"""


class Student:
    """student class"""
    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def class_to_json(obj):
        """returns the dictionary description with simple data structure"""
        return obj.__dict__
