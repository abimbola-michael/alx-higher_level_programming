#!/usr/bin/python3
""" function that adds 2 integers """


def add_integer(a, b=98):
    """a function that adds 2 integers
    Args:
        a: first input
        b: second input

    Raises:
        TypeError: If either of a or b is a non-integer and a non-float.
    """
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")

    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")

    return (a + b)
