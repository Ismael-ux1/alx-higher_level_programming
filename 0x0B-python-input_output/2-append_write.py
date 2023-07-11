#!/usr/bin/python3
""" A function that appends a string at the end of a text. """


def append_write(filename="", text=""):
    """
    Append a string to the end of a text file (UTF-8) and return the numebr of;
    characters added.

    Args:
       filename (str): The name of the text file to append.
        text (str): The string to be appended to the file.

      Returns:
        int: The number of characters added to the file.

    Raises:
        None

    Usage:
        characters_added = append_write("filename.txt", "Hilberton Schools!")
        print(characters_added)  # Print the number of characters added
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        characters_added = file.write(text)
        return characters_added
