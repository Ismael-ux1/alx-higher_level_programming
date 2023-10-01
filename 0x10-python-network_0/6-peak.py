#!/usr/bin/python3
""" A function that finds a peak in a list of unsorted integers. """


def find_peak(list_of_integers):
    """
    find a peak in a list of unsorted ingeres.

    A peak is an element that is not smaller than its neighbors.
    This function finds one peak, not necessarily the highest peak.
    """

    # If the list is empty, return None
    if not list_of_integers:
        return None

    # Initialize low and high pointers to the start and end of the list
    low = 0
    high = len(list_of_integers) - 1

    # While the search space contain more than one element
    while low < high:
        # Calculate the middle index
        mid = (low + high) // 2

        # If the middle element is greater than the next element,
        # then the peak must be in the left of the list
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            high = mid
        else:
            # Otherwise, the peak must be in the right half
            low = mid + 1

    # When the search space has been reduced to one element,
    # return that element as it is a peak
    return list_of_integers[low]
