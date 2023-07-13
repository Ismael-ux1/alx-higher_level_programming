#!/usr/bin/python3
"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer

class MaxIntegerTest(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_one_element_list(self):
        self.assertEqual(max_integer([1]), 1)

    def test_list_with_multiple_elements(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_list_with_duplicates(self):
        self.assertEqual(max_integer([1, 1, 2, 3, 4]), 4)

    def test_list_with_negative_elements(self):
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)

    def test_list_with_mixed_elements(self):
        self.assertEqual(max_integer([1, 2, 3, -4, 5]), 5)

if __name__ == '__main__':
    unittest.main()
