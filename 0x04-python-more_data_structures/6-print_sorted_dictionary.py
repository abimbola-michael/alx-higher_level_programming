#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """a function that prints a dictionary by ordered keys"""
    sorted_list = sorted(a_dictionary.keys())
    for key in sorted_list:
        print("{}: {}".format(key, a_dictionary[key]))
