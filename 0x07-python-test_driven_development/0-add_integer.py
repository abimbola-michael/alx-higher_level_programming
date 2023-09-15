#!/usr/bin/python3
""" function that adds 2 integers """


def add_integer(a, b=98):
    """a function that adds 2 integer
    a and b must be integers or floats, otherwise
    raise a TypeError exception with the message a must be
    an integer or b must be an integer
    Raises:
        TypeError: If either of a or b is a non-integer and a non-float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return (a + b)
