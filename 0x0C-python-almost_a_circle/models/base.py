#!/usr/bin/python3
"""Base Class"""
import json


class Base:
    """Base class
    __nb_objects(int):
        number of class instances
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Class Initialization"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation
        of list_dictionaries"""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of
        list_objs to a file"""

        filename = cls.__name__ + ".json"
        with open(filename, "w") as fl:
            if list_objs is None:
                fl.write("[]")
            else:
                list_dictionaries = [obj.to_dictionary() for obj in list_objs]
                json_string = Base.to_json_string(list_dictionaries)
                fl.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string
        representation json_string"""

        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""

        if dictionary and len(dictionary) != 0:
            if cls.__name__ == "Rectangle":
                new_cls = cls(3, 3)
            else:
                new_cls = cls(3)
            new_cls.update(dictionary)
        return new_cls

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""

        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as fl:
                list_dictionaries = Base.from_json_string(json.read())
            return [
                    cls.create(dictionary) for dictionary in list_dictionaries
                    ]
        except IOError:
            return []
