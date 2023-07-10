#!/usr/bin/python3
"""a class Square that inherits from Rectangle (9-rectangle.py)
"""
Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """a class Square that inherits from Rectangle"""

    def __init__(self, size):
        """
        A square initialization
        Args:
            size (int): square size
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
