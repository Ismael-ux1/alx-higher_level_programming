#!/usr/bin/python3
def replace_in_list(my_list, idx, new_element):
    """Replace an element of a list at a specific position
    Args:
    my_list: the list in which to replace an element
    idx: the index at which to replace the element
    element: the new element to be placed in specific position
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = new_element
    return my_list
