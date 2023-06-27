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
        """Getter Property"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter Property"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Function used to calculate area"""
        return (self.__size * self.__size)

    def my_print(self):
        """Function used to print a # square"""
        if self.__size == 0:
            print("")
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print("#", end="")
            print("")
