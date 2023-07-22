#!/usr/bi/python3
""" Test case for base class """

import unittest
import json
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


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

    def test_to_json_string_empty_list(self):
        # Test to_json_string with an empty list
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_to_json_string_none_list(self):
        # Test to_json_string with a None list
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_to_json_string(self):
        # Test to_json_string with a list of dictionaries
        list_dictionaries = [
            {"id": 1, "name": "Alice"},
            {"id": 2, "name": "Bob"}
            ]
        json_string = Base.to_json_string(list_dictionaries)
        self.assertEqual(json_string, '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]')

    def test_from_json_string_empty(self):
        # Test when the JSON string is empty
        json_string = ""
        self.assertEqual(Base.from_json_string(json_string), [])

    def test_from_json_string_none(self):
        # Test when the JSON string is None
        json_string = None
        self.assertEqual(Base.from_json_string(json_string), [])

    def test_from_json_string(self):
        # Test when the JSON string represents a list of dictionaries
        json_string = '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]'
        expected_result = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
        self.assertEqual(Base.from_json_string(json_string), expected_result)

    def test_base_save_to_file(self):
        # Test save_to_file method with list of Rectangles
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        rectangles = [r1, r2]
        Rectangle.save_to_file(rectangles)
        with open("Rectangle.json", "r") as file:
            data = json.load(file)
            self.assertEqual(data, [r1.to_dictionary(), r2.to_dictionary()])
        os.remove("Rectangle.json")

        # Test save_to_file method with list of Squares
        s1 = Square(5)
        s2 = Square(9, 3, 1)
        squares = [s1, s2]
        Square.save_to_file(squares)
        with open("Square.json", "r") as file:
            data = json.load(file)
            self.assertEqual(data, [s1.to_dictionary(), s2.to_dictionary()])
        os.remove("Square.json")

    def test_create_rectangle(self):
        # Create a dictionary with attributes for Rectangle
        rectangle_dict = {"width": 4, "height": 6, "x": 2, "y": 3}

        # Create an instance of Rectangle using create method
        rectangle_instance = Rectangle.create(**rectangle_dict)

        # Check if the instance is of the correct class
        self.assertIsInstance(rectangle_instance, Rectangle)

        # Check if the attributes are set correctly
        self.assertEqual(rectangle_instance.width, 4)
        self.assertEqual(rectangle_instance.height, 6)
        self.assertEqual(rectangle_instance.x, 2)
        self.assertEqual(rectangle_instance.y, 3)

    def test_create_square(self):
        # Create a dictionary with attributes for Square
        square_dict = {"size": 5, "x": 1, "y": 2}

        # Create an instance of Square using create method
        square_instance = Square.create(**square_dict)

        # Check if the instance is of the correct class
        self.assertIsInstance(square_instance, Square)

        # Check if the attributes are set correctly
        self.assertEqual(square_instance.size, 5)
        self.assertEqual(square_instance.x, 1)
        self.assertEqual(square_instance.y, 2)

    def test_create_invalid_class(self):
        # Create a dictionary with attributes for an unknown class
        invalid_dict = {"attribute1": 10, "attribute2": 20}

        # Create an instance using create method, for an unknown class
        instance = Base.create(**invalid_dict)

        # Check if the instance is None, as class is unknown
        self.assertIsNone(instance)

        def test_load_from_file(self):
            # Create some instances and save them to a JSON file
            r1 = Rectangle(3, 5, 1)
            r2 = Rectangle(4, 2)
            s1 = Square(2)
            s2 = Square(3, 1, 4)
            instances_list = [r1, r2, s1, s2]

            filename = "TestLoadFromFile.json"
            Base.save_to_file(instances_list)

            # Load instances from the JSON file
            loaded_instances = Base.load_from_file()

            # Clean up the created file
            os.remove(filename)

            # Check if the loaded instances are of the correct types
            self.assertIsInstance(loaded_instances[0], Rectangle)
            self.assertIsInstance(loaded_instances[1], Rectangle)
            self.assertIsInstance(loaded_instances[2], Square)
            self.assertIsInstance(loaded_instances[3], Square)

            # Check if the loaded instances have the correct attributes
            self.assertEqual(loaded_instances[0].width, 3)
            self.assertEqual(loaded_instances[0].height, 5)
            self.assertEqual(loaded_instances[0].x, 1)
            self.assertEqual(loaded_instances[0].y, 0)
            
            self.assertEqual(loaded_instances[1].width, 4)
            self.assertEqual(loaded_instances[1].height, 2)
            self.assertEqual(loaded_instances[1].x, 0)
            self.assertEqual(loaded_instances[1].y, 0)
            
            self.assertEqual(loaded_instances[2].size, 2)
            self.assertEqual(loaded_instances[2].x, 0)
            self.assertEqual(loaded_instances[2].y, 0)

            self.assertEqual(loaded_instances[3].size, 3)
            self.assertEqual(loaded_instances[3].x, 1)
            self.assertEqual(loaded_instances[3].y, 4)

        def test_save_to_file_csv(self):
            # Test code for save_to_file_csv method with CSV format
            r1 = Rectangle(3, 5, 1)
            r2 = Rectangle(4, 6, 2)
            Rectangle.save_to_file_csv([r1, r2])
            filename = "Rectangle.csv"
            self.assertTrue(os.path.isfile(filename))

    def test_load_from_file_csv(self):
        # Test code for load_from_file_csv method with CSV format
        filename = "Rectangle.csv"
        if os.path.isfile(filename):
            os.remove(filename)

        r1 = Rectangle(3, 5, 1)
        r2 = Rectangle(4, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])

        rectangles = Rectangle.load_from_file_csv()
        self.assertIsInstance(rectangles, list)
        self.assertTrue(all(isinstance(r, Rectangle) for r in rectangles))


if __name__ == '__main__':
    unittest.main()
