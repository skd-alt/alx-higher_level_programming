#!/usr/bin/python3
# models/base.py
"""Unittests for Base()."""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ unittests for Base class."""

    def test_with_id(self):
        """Test an with id"""
        b1 = Base(12)
        self.assertEqual(b1.id, 12)

    def test_without_id(self):
        """Test an without id"""
        b2 = Base()
        self.assertEqual(b2.id, 1)

    def test_with_string(self):
        """Test an with string"""
        b3 = Base("a")
        self.assertEqual(b3.id, "a")

    def test_with_large_int(self):
        """Test an with large int"""
        b3 = Base(11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111)
        self.assertEqual(b3.id, 11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111)
