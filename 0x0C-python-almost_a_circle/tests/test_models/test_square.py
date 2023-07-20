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

    def test_square_update(self):
        # Create a square
        square = Square(5, 2, 3, 1)

        # Update using *args
        square.update(2, 7)

        # Check the updated attributes
        self.assertEqual(square.id, 2)
        self.assertEqual(square.width, 7)
        self.assertEqual(square.height, 7)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

        # Update using **kwargs
        square.update(size=10, y=4)

        # Check the updated attributes
        self.assertEqual(square.id, 2)
        self.assertEqual(square.width, 10)
        self.assertEqual(square.height, 10)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 4)

    def test_square_to_dictionary(self):
        # Create a square with size=5, x=2, y=3, and id=1
        square = Square(5, 2, 3, 1)

        # Get the dictioanry representation
        square_dict = square.to_dictionary()

        # Check the dictionary values
        self.assertEqual(square_dict['id'], 1)
        self.assertEqual(square_dict['size'], 5)
        self.assertEqual(square_dict['x'], 2)
        self.assertEqual(square_dict['y'], 3)


if __name__ == "__main__":
    unittest.main()
