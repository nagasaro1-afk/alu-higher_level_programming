#!/usr/bin/python3
"""Defines a class_to_json function."""


def class_to_json(obj):
    """Return the dictionary description of an object for serialization.

    Args:
        obj: An instance of a class whose attributes are all
            serializable (list, dict, str, int, bool).

    Returns:
        dict: The object's attribute dictionary.
    """
    return obj.__dict__
