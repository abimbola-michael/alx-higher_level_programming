#!/usr/bin/python3
"""a class Rectangle that inherits from BaseGeometry
(7-base_geometry.py). (task based on 8-rectangle.py)
"""
BaseGeometry = __import__('7-base_geometry.py').BaseGeometry


class Rectangle(BaseGeometry):
    """Class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """
        Used to validate as int
        Args:
            width (int): input width
            height (int): input height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
