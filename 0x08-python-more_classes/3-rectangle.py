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

    def area(self):
        """Calculates the area of a rectangle"""

        return (self.__width * self.__height)

    def perimeter(self):
        """Calculates the perimeter of a rectangle"""

        if self.__width == 0 or self.__height == 0:
            return 0

        return (2 * (self.__width + self.__height))

    def __str__(self):
        "String representation of rectangle class"""

        if self.__width == 0 or self.__height == 0:
            return ""

        print_list = []

        for i in range(self.__height):
            [print_list.append("#") for j in range(self.__width)]
            if i != self.__height - 1:
                print_list.append("\n")
        string = "".join(print_list)

        return string
