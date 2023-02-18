#!/usr/bin/python3
"""Fourth"""

import json


def from_json_string(my_str):
    """Creates a object from a JSON string
    Args:
        my_str (str): JSON string to objectify
    Returns:
        object of JSON string
    """
    return json.loads(my_str)
