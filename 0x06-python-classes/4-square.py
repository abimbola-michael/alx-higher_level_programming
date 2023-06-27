#!/usr/bin/python3
"""Defines a square class"""


class Square:
    """Define a Square"""
    def __init__(self, size=0):
        """Instantiation with optional
        Args:
            size (int): size of the square
        """
        self.size = size

    @property
    def size(self):
        """Getter propery"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter property"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates area """
        return (self.__size * self.__size)
