#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """a function that returns a new dictionary with all values
    multiplied by 2"""
    new_dictionary = a_dictionary.copy()
    keys = list(new_dictionary.keys())
    for key in keys:
        new_dictionary[key] = a_dictionary[key] * 2
    return new_dictionary
