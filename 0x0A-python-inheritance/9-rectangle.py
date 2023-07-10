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
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Calculates the area of the rectangle class
        """

        return self.__width * self.__height

    def __str__(self):
        """
        String representation of the class
        """

        string = "[{}]".format(self.__class__.__name__)
        string += " {}/{}".format(self.__width, self.__height)
        return string
