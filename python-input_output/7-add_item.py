#!/usr/bin/python3
"""a script that adds all arguments to a Python list"""

import json

save_to_json_file =__import__('5-save_to_json_file').save_to_json_file
load_from_json_file =__import__('6-load_from_json_file').load_from_json_file


if isfile("add_item.json"):
    new_list = load_from_json_file("add_item.json")
else:
    new_list = []