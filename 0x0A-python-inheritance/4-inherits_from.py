#!/usr/bin/python3
"""a function that returns True if the object is an instance of
a class that inherited (directly or indirectly) from the
specified class ; otherwise False"""


def inherits_from(obj, a_class):
     """a function that check for instance of a class
    Args:
        obj (any): Class to check
        a_class (type): class to check instance with
    Returns:
        True if the object is exactly an instance of the specified
        class or if the object is an instance of a class that inherited
        from, the specified class otherwise False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
