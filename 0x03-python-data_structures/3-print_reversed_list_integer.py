#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Print all integers list in reverse order
    Args:
    my_list: list of integers
    Return:
    None
    """
    for i in reversed(my_list):
        print("{:d}".format(i))
