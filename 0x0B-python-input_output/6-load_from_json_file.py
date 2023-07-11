#!/usr/bin/python3
"""a function that creates an Object from a JSON file"""
import json

def load_from_json_file(filename):
    """function that creates an Object from a json file"""

    with open(filename) as fl:
        string = json.load(fl)
        return string
