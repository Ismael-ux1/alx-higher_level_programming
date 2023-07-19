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


if __name__ == "__main__":
    unittest.main()
