#!/usr/bin/python3
"""a function that creates an Object from a JSON file"""


def load_from_json_file(filename):
    """function that creates an Object from a json file"""

    with open(filename, "r") as fl:
        json.load(fl)
