#!/usr/bin/python3
"""a class Student that defines a student by"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Initializes new student"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""

        if type(attrs) == list and all(type(item) == str for item in attrs):
            return {
                    item: getattr(
                        self, item
                        ) for item in attrs if hasattr(self, item)
                    }
        return self.__dict__
