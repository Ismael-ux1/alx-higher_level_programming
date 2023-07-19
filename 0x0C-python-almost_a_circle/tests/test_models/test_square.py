#!/usr/bin/python3
import unittest
from models.square import Square
from models.rectangle import Rectangle


class TestSquare(unittest.TestCase):
    def test_square_inherits_from_rectangle(self):
        self.assertIsInstance(Square(1), Rectangle)

    def test_square_constructor(self):
        s = Square(1)
        self.assertEqual(s.width, 1)
        self.assertEqual(s.height, 1)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_square_str(self):
        s = Square(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (4) 2/3 - 1")


if __name__ == "__main__":
    unittest.main()
