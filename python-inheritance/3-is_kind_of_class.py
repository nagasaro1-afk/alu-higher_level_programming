#!/usr/bin/python3
"""Defines an is_kind_of_class function."""


def is_kind_of_class(obj, a_class):
    """Check if obj is an instance of a_class or a subclass of it.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        True if obj is an instance of a_class or a subclass, else False.
    """
    return isinstance(obj, a_class)
