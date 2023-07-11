#!/usr/bin/python3
""" A function that writes a string to a text file and returns the number """


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF-8) and return the number;
    of characters written.

    Args:
        filename (str): The name of the text file to write.
        text (str): The string to be written to the file.

    Returns:
        int: The number of character written to the file.

     Raises:
        None

    Usage:
        characters_written = write_file("filename.txt", "Hilborton School")
        print(characters_written)
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        characters_written = file.write(text)
        return characters_written
