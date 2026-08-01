#!/usr/bin/python3
"""Defines a save_to_json_file function."""
import json


def save_to_json_file(my_obj, filename):
    """Write an Object to a text file using its JSON representation.

    Args:
        my_obj: The object to serialize.
        filename (str): The name of the file to write to.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
