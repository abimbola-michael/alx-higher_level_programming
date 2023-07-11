#!/usr/bin/python3
"""a function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """function that reads utf8 file"""

    with open(filename, encoding="utf-8") as fl:
        print(fl.read(), end="")
