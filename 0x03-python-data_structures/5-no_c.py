#!usr/bin/python3
def no_c(my_string):
    """
  Removes all characters c and C from a string.

  Args:
    my_string: The string to be modified.

  Returns:
    A new string with all characters c and C removed.
    """
    my_string = my_string.translate({ord(i): None for i in "Cc"})
    return (my_string)
