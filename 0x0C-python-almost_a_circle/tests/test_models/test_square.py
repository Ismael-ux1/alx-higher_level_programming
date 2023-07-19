#!/usr/bin/python3
import unittest
from models.square import Square
from models.rectangle import Rectangle


class TestSquare(unittest.TestCase):

    def test_square_attributes(self):
        # Create a square
        square = Square(5, 2, 3, 1)

        # Check the attributes
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 1)

    def test_square_str(self):
        # Create a square
        square = Square(5, 2, 3, 1)

    def test_square_size_getter(self):
        # Create a square
        square = Square(5, 2, 3, 1)

        # Check the getter for the size
        self.assertEqual(square.size, 5)

    def test_square_size_setter(self):
        # Create a square
        square = Square(5, 2, 3, 1)

        # Update the size using the setter
        square.size = 10

        # Check the updated size and the width and height are equal
        self.assertEqual(square.size, 10)
        self.assertEqual(square.width, 10)
        self.assertEqual(square.height, 10)


if __name__ == "__main__":
    unittest.main()
