#!/usr/bin/python3
""""function that creates an Object"""

import json


def load_from_json_file(filename):
    with open(filename, "r") as f:
        json.load(f)
