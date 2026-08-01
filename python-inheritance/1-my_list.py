#!/usr/bin/python3
"""Defines a MyList class that inherits from list."""


class MyList(list):
    """Represent a list with an extra print_sorted method."""

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        print(sorted(self))
