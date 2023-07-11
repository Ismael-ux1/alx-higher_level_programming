#!/usr/bin/python3
""" A function that reads a text and prints it. """


def read_file(filename=""):
    """
    Read and print the contents of a text file to stdout.

    Args:
        filename (str): The name of the text file to be read.

    Returns:
        None

    Raises:
        None

    Usage:
        read_file("filename.txt")
    """
    with open(filename, encoding="utf-8") as file:
        for line in file:
            print(line, end="")
