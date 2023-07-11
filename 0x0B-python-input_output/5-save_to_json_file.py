#!/usr/bin/python3
"""a function that writes an Object to a text file, using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file using json"""

    with open(filename, "w") as fl:
        json.dump(my_obj, fl)
