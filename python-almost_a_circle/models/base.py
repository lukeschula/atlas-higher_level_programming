#!/usr/bin/python3
""""almost a circle start"""

import json


class Base:
    """writing the first class, Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """eturns the JSON string representation of
        list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """rites the JSON string representation of
        list_objs to a file"""
        filename = cls.__name__ + ".json"
        newlist = []
        if list_objs:
            for objects in list_objs:
                newdict = objects.to_dictionary()
                result = append(newdict)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(result))
