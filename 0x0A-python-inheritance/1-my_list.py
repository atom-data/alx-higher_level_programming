#!/usr/bin/python3
"""Defining the class MyList"""


class MyList(list):
    """Subclass of list"""

    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
