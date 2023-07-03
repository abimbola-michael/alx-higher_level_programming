#!/usr/bin/python3
"""a class Rectangle that defines a rectangle by:
(based on 0-rectangle.py)"""


class Rectangle:
    """A Rectangle class with instance
    Attributes:
        number_of_instances (int):
        used for calculating number of instances
        print_symbol (any):
        used tok pint symbol
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes Rectangle
        Args:
            width (int): rectangle width
            height (int): rectangle height
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
        print_string = str(self.print_symbol)

        for i in range(self.__height):
            [print_list.append(print_string) for j in range(self.__width)]
            if i != self.__height - 1:
                print_list.append("\n")
        string = "".join(print_list)

        return string

    def __repr__(self):
        """Representation of the Rectangle class"""

        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """Delete representation of the Rectangle class"""

        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Checks biggest rectangle based on the area"""

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
