#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    Converts a Roman numeral to an integer.

    Args:
        roman_string (str): The Roman numeral string.

    Returns:
        int: The corresponding integer value.

    """
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                  'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = float('inf')
    for char in roman_string:
        value = roman_dict[char]
        result += value
        if value > prev_value:
            result -= 2 * prev_value
        prev_value = value
    return result
