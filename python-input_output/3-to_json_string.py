#!/usr/bin/python3
"""Third"""

import json


def to_json_string(my_obj):
    """Creates a JSON representation of an object
    Args:
        my_obj (object): object to JSONify
    Returns:
        string version of JSON representation
    """
    return json.dumps(my_obj)
