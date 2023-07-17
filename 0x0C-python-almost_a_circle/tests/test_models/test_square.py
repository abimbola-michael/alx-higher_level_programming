#!/usr/bin/python3
"""Square class Test"""
import unittest
import os

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSqaure(unittest.TestCase):
    """Sqaure Class Test"""

    def test_no_arg(self):
        sqr1 = Square()
        sqr2 = Square()

        self.assertEqual(sqr1.id, sqr2.id - 1)

    def test_none_id(self):
        sqr1 = Square(None)
        sqr2 = Square(None)

        self.assertEqual(sqr1.id, sqr2.id - 1)

    def test_three_bases(self):
        sqr1 = Square()
        sqr2 = Square()
        sqr3 = Square()

        self.assertEqual(sqr1.id, sqr3.id - 2)

    def test_real_id(self):
        sqr = Square(4)

        self.assertEqual(sqr.id, 4)

if __name__ == "__main__":
    unittest.main()
