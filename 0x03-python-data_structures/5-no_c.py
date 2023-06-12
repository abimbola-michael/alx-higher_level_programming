#!/usr/bin/python3
def no_c(my_string):
    """a function that removes all characters
    c and C from a string"""
    new_string_list = [x for x in my_string if x != 'c' and x != 'C']
    new_string = "".join(new_string_list)
    return new_string
