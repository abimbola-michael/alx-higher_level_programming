#!/usr/bin/python3
"""a function that returns True if the object is exactly an instance
of the specified class ; otherwise False"""


def is_same_class(obj, a_class):
    """a function that check for instance of a class
    Args:
        obj (any): Class to check
        a_class (type): class to check instance with
    Returns:
        True if the object is exactly an instance of the specified class
        otherwise False
    """
    if type(obj) == a_class:
        return True
    else:
        return False
