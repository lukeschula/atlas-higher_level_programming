#!/usr/bin/python3
"""a class Student that defines a student by:
(based on 10-student.py)"""


class Student:
    """student class"""
    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """that retrieves a dictionary representation of a Student instance"""
        if attrs is not None:
            key = {}
            for el in attrs:
                if el in self.__dict__:
                    key[el] = self.__dict__[el]
            return key
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for el in json:
            self.__dict__[el] = json[el]
