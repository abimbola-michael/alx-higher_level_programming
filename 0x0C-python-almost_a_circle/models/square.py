#!/usr/bin/python3
"""A class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class Initialization"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.size
                )

    @property
    def size(self):
        """Size getter"""

        return self.width

    @size.setter
    def size(self, value):
        """Size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates the class"""

        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
                i += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs:
                if k == "id":
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif i == "width":
                    self.width = v
                elif i == "height":
                    self.height = v
                elif i == "x":
                    self.x = v
                elif i == "y":
                    self.y = v

    def to_dictionary(self):
        """Dictionary representation of class"""

        return {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y,
                }
