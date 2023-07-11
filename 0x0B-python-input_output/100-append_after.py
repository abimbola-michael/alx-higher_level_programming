#!/usr/bin/python3
"""a function that inserts a line of text to a file, after each line
containing a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """ function that inserts a line of text to a file, after each line"""

    text = ""
    with open(filename) as fl:
        for line in fl:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as fl:
        fl.write(text)
