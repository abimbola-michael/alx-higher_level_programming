#!/usr/bin/python3
"""a class Rectangle that defines a rectangle by:
(based on 0-rectangle.py)"""


class Rectangle:
    """A Rectangle class with instance"""

    def __init__(self, width=0, height=0):
        """Initializes Rectangle
        Args:
            width (int): rectangle width
            height (int): rectangle height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for the width"""

        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the height"""

        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
