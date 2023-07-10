#!/usr/bin/python3
""" a class MyInt that inherits from int"""


class MyInt(int):
    """a class MyInt that inherits from int"""

    def __eq__(self, value):
        """Use == with != """

        return self.real != value

    def __ne__(self, value):
        """Use == with != """

        return self.real == value
