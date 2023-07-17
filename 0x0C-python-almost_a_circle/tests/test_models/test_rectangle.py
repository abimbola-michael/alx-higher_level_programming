#!/usr/bin/python3
"""Rectangle class Test"""
import unittest
import os

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
    """Rectangle Class Test"""

    def test_no_arg(self):
        rect1 = Rectangle()
        rect2 = Rectangle()

        self.assertEqual(rect1.id, rect2.id - 1)

    def test_none_id(self):
        rect1 = Rectangle(None)
        rect2 = Rectangle(None)

        self.assertEqual(rect1.id, rect2.id - 1)

    def test_three_bases(self):
        rect1 = Rectangle()
        rect2 = Rectangle()
        rect3 = Rectangle()

        self.assetEqual(rect1.id, rect3.id - 2)

    def test_real_id(self):
        rect = Rectangle(4)

        self.assertEqual(rect, 4)

if __name__ == "__main__":
    unittest.main()
