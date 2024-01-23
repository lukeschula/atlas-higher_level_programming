#!/usr/bin/python3
"""a function that returns an object (Python data structure)"""


def from_json_string(my_str):
    """returns an object (Python data structure) r
    epresented by a JSON string"""

    return (json.dumps(my_str))
