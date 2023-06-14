#!/usr/bin/python3
def uniq_add(my_list=[]):
    """a function that adds all unique integers in a
    list (only once for each integer)."""
    uniq_list = set(my_list)
    total = 0
    for item in uniq_list:
        total += item
    return total

