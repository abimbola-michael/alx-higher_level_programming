#!/usr/bin/python3
"""Unit Test for max_integer"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class MaxIntegerTest(unittest.TestCase):
    """ unittests for the function def max_integer(list=[]):
    """

    def ordered_list_test(self):
        """ Testing for ordered list """
        ord_list = [2, 4, 6, 8, 10]
        self.assertEqual(max_integer(ord_list), 10)

    def unordered_list_test(self):
        """ Testing for unordered list """
        unord_list = [6, 2, 9, 4, 8]
        self.assertEqual(max_integer(unord_list), 9)

    def empty_list_test(self):
        """ Testing for empty list"""
        emp_list = []
        self.assertEqual(max_integer(emp_list), None)

    def float_list_test(self):
        """ Testing for float list"""
        float_list = [3.5, 4.5, 9.0, 4.0]
        self.assertEqual(max_integer(float_list), 9.0)

    def negative_list_test(self):
        """ Testing for negative list"""
        neg_list = [-3.5, -4.5, -9.0, -4.0]
        self.assertEqual(max_integer(neg_list), -3.5)

    def string_list_test(self):
        """ Testing for string list"""
        string_list = ["Michael", "Abimbola"]
        self.assertEqual(max_integer(string_list), "Michael")

    def mixed_list_test(self):
        """ Testing for mixed list"""
        mixed_list = [2, 9.5, 5.6, 9, 6]
        self.assertEqual(max_integer(mixed_list), 9.5)


if __name__ == "__main__":
    unittest.main()
