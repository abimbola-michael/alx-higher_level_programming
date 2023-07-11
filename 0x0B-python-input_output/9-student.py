#!/usr/bin/python3
"""a class Student that defines a student by"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Initializes new student"""
        
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance"""

        return self.__dict__
