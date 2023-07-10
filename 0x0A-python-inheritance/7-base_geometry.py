#!/usr/bin/python3
"""a class BaseGeometry (based on 6-base_geometry.py)"""


class BaseGeometry:
    """A class that calculates area"""

    def area(self):
        """Calculate Area"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the integer
        Args:
            name (str): input name
            value (any): input value
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less or equal to 0
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
