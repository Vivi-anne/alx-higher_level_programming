#!/usr/bin/python3
"""Defines an inherited list class MyList"""


class MyList(list):
    """subclass of list"""
    def __init__(self):
        """Initiates MyList class"""
        super().__init__()

    def print_sorted(self):
        """Print list in sorted ascending order"""
        print(sorted(self))
