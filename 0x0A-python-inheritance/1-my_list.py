#!/usr/bin/python3
""" A function that prints the list in ascending order """


class MyList(list):
    def print_sorted(self):
        """ Print the list in ascending order. """
        print(sorted(self))
