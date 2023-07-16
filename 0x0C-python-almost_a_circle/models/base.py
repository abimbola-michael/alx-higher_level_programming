#!/usr/bin/python3
"""Base Class"""


class Base:
    """Base class"""

    __nb_objects = 0
    
    def __init__(self, id=None):
        """Class Initialization"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
