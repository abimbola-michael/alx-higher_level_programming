#!/usr/bin/python3
"""Base class Test"""
import unittest
import os

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Base Class Test"""

    def test_no_arg(self):
        base1 = Base()
        base2 = Base()

        self.assertEqual(base1.id, base2.id - 1)

    def test_none_id(self):
        base1 = Base(None)
        base2 = Base(None)

        self.assertEqual(base1.id, base2.id - 1)

    def test_three_bases(self):
        base1 = Base()
        base2 = Base()
        base3 = Base()

        self.assetEqual(base1.id, base3.id - 2)

    def test_real_id(self):
        base = Base(4)

        self.assertEqual(base, 4)

if __name__ == "__main__":
    unittest.main()
