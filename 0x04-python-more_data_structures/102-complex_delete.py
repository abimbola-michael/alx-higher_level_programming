#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """a function that deletes keys with a specific value in a dictionary"""
    keys_list = list(a_dictionary.keys())

    for key in keys_list:
        if value == a_dictionary[key]:
            del a_dictionary[key]
    return a_dictionary
