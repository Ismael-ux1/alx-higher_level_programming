#!/usr/bin/python3
def element_at(my_list, idx):
    """Retrieves an element from the list
       Args:
       my_list: A list of integers
       idx: the index of the element to retrive
       """
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
