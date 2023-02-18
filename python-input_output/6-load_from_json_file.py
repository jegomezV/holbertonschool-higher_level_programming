#!/usr/bin/python3
"""Sixth"""

import json


def load_from_json_file(filename):
    """Creates a Python object from JSON file
    Args:
        filename (str): string of path to file
    Returns:
        Python object
    """
    data = None
    with open(filename, 'r', encoding='utf-8') as json_data:
        data = json.load(json_data)
    return data
