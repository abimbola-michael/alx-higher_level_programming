#!/usr/bin/python3
class Square:
    """Define a Square"""
    def __init__(self, size=0):
        """Instantiation with optional
        Args:
            size (int): size of the square
            position (int, int): tuple position of the new square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return (self.__size)

    @position.setter
    def position(self, value):
        """sets a new position for the square"""
        if not isinstance(value, tuple) or len(value) != 2
        or not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.position = value

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            print("")
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print("#", end="")
            print("")
