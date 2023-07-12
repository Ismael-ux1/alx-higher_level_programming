#!/usr/bin/python3
""" A script that adds all arguments to a Python list """

import sys
import json


def save_to_json_file(my_obj, filename):
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(my_obj, file, ensure_ascii=False)


def load_from_json_file(filename):
    with open(filename, encoding="utf-8") as file:
        obj = json.load(file)
        return obj

# Read the existing items from the file (if any)


try:
    items = load_from_json_file("add_item.json")
except FileNotFoundError:
    items = []

# Add the command-line arguments to the list
items.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(items, "add_item.json")
