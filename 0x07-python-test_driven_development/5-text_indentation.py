#!/usr/bin/python3


"""
A function that  Prints a text with 2 new lines
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':' characters.

    Args:
        text (str): The text to be indented.

    Raises:
        TypeError: If text is not a string.

    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Remove leading and trailing whitespace from the text
    text = text.strip()

    # Iterate over each character in the text
    for char in text:
        print(char, end="")

        # Check if the character is '.', '?', or ':'
        if char in ['.', '?', ':']:
            print("\n\n", end="")
