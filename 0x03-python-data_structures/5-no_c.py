#!usr/bin/python3
def no_c(my_string):
    """
    Removes all characters c and C from a string

    Args:
    my_string: The string to be modified.

    Returns:
    A new string with all characters c and C removed.
    """
    new_string = ''.join(char for char in my_string if char.lower() != 'c')
    
    return new_string
