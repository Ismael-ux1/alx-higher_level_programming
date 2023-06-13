#!/usr/bin/python3
def new_in_list(my_list, idx, element):

    """
  Replaces an element in a list at a specific positio.

  Args:
    my_list: The list to be modified.
    idx: The index of the element to be replaced.
    element: The new element to be inserted.

  Returns:
    A copy of the list with the element index replaced
    """
    if(my_list is not None):
        m_list = my_list.copy()
        if idx < 0 or idx >= len(my_list):
            return my_list
        else:
            m_list[idx] = element
            return m_list
