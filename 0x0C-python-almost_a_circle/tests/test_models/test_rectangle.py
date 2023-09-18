#!/usr/bin/python3
# models/Rectangle.py
"""Unittests for Rectangle"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ unittests for Rectangle class."""

    def test_two_arg(self):
        """Test with two args"""
        r1 = Rectangle(5, 3)
        self.assertEqual(r1.id, 3)

    def test_three_arg(self):
        """Test with 3 args"""
        r2 = Rectangle(5, 3, 1)
        self.assertEqual(r2.id, 2)

    def test_four_arg(self):
        """Test with 4 args"""
        r3 = Rectangle(5, 3, 1, 5)
        self.assertEqual(r3.id, 1)

    def test_five_arg(self):
        """Test with 5 args"""
        r4 = Rectangle(5, 3, 1, 2, 17)
        self.assertEqual(r4.id, 17)

    def test_null(self):
        """Test no agrs"""
        with self.assertRaises(TypeError):
          r5 = Rectangle()

    def test_one_arg(self):
        """Test one arg"""
        with self.assertRaises(TypeError):
          r6 = Rectangle(5)

    def test_more_than_five(self):
        """Test GREATER THAN 5 agrs"""
        with self.assertRaises(TypeError):
            r7 = Rectangle(5, 3, 1, 2, 17, 4)
