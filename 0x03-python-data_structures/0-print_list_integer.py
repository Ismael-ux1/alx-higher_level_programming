#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """prints all the integer in the list

       Args:
       my_list: A list of integers
       Returns:
       None.
       """
    for num in my_list:
        print("{:d}".format(num))
