#!/usr/bin/python
""" Test case for rectangle class. """

import unittest
from models.rectangle import Rectangle
from unittest.mock import patch
import io


class TestRectangle(unittest.TestCase):

    def test_rectangle_attributes(self):
        # Creat a rectangle
        rect = Rectangle(10, 20, 2, 4, 1)

        # Check the attributes
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 20)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 4)
        self.assertEqual(rect.id, 1)

    def test_rectangle_attribute_setters(self):
        # Create a rectangle
        rect = Rectangle(10, 20, 2, 4, 1)

        # Set new values using the setters
        rect.width = 15
        rect.height = 25
        rect.x = 5
        rect.y = 8

        # Check the updated attrubutes
        self.assertEqual(rect.width, 15)
        self.assertEqual(rect.height, 25)
        self.assertEqual(rect.x, 5)
        self.assertEqual(rect.y, 8)

    def test_rectangle_area(self):
        # Create a rectangle
        rect = Rectangle(10, 20)

        # Calculate the area
        area = rect.area()

        # Check the calculated area
        self.assertEqual(area, 200)

    def test_rectangle_display(self):
        # Create a rectangle
        rect = Rectangle(3, 4)

        # Capture the printed output
        captured_output = io.StringIO()
        with patch('sys.stdout', new=captured_output):
            # Call the display method
            rect.display()

    def test_rectangle_str(self):
        # Create a rectangle
        rect = Rectangle(5, 10, 2, 3, 1)

        # Check the string representation
        self.assertEqual(str(rect), "[Rectangle] (1) 2/3 - 5/10")

    def test_rectangle_invalid_values(self):
        # Create a rectangle with invalid attribute values
        with self.assertRaises(TypeError):
            rect = Rectangle("invalid", 20, 2, 4, 1)

        with self.assertRaises(ValueError):
            rect = Rectangle(-10, 20, 2, 4, 1)

        with self.assertRaises(TypeError):
            rect = Rectangle(10, "invalid", 2, 4, 1)

        with self.assertRaises(ValueError):
            rect = Rectangle(10, 0, 2, 4, 1)

        with self.assertRaises(TypeError):
            rect = Rectangle(10, 20, "invalid", 4, 1)

        with self.assertRaises(ValueError):
            rect = Rectangle(10, 20, -2, 4, 1)

        with self.assertRaises(TypeError):
            rect = Rectangle(10, 20, 2, "invalid", 1)

        with self.assertRaises(ValueError):
            rect = Rectangle(10, 20, 2, -4, 1)


if __name__ == '__main__':
    unittest.main()
