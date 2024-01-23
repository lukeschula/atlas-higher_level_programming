#!/usr/bin/python3
"""a class Student that defines a student by:
(based on 9-student.py)"""


class Student:
    """student class"""
    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """that retrieves a dictionary representation of a Student instance"""
        return self.__dict__
