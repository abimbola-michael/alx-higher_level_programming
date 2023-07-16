#!/usr/bin/python3
"""Rectangle Class"""
Base = __import__('base.py').Base



class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class Initialization"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Width getter"""
        
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
    
    @property
    def height(self):
        """Height getter"""
        
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter"""
        
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter"""
        
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculates the area of the rectangle"""
        
        return self.width * self.height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        
        if self.width == 0 or self.height == 0:
            print("")
            return
        [print("") for y in range(self.y)]
        for i in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for j in range(self.width)]
            print("")

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height
                )



