#!/usr/bi/python3
""" Test case for base class """

import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_base_id_increment(self):
        # Create multiple instance of Base
        b1 = Base()
        b2 = Base()
        b3 = Base()

        # Check if IDs are increnented correctly
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

        def test_base_custom_id(self):
            # Create an instance of base with a custom ID
            b = Base(10)

            # Check if the custom ID is assigned correctly
            self.assertEqual(b.id, 10)

        def test_to_json_string_empty(self):
            """ Test to_json_string with an empty list. """
            self.assertEqual(Base.to_json_string(None), "[]")
            self.assertEqual(Base.to_json_string([]), "[]")

        def test_to_json_string(self):
            """ Test to_json_string with a non empty list of dictionaries. """
            json_string = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': "Bob"}]
            json_string = Base.to_json_string(json_string)
        self.assertEqual(type(json_string), str)
        self.assertEqual(json_string, '[{id": 1, "name": "Alice"}, '
                         '{"id": 2, "name": "Bob"}]')


if __name__ == '__main__':
    unittest.main()
