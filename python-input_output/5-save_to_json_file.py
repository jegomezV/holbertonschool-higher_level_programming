#!/usr/bin/python3
"""Fifth"""

import json


def save_to_json_file(my_obj, filename):
    """Writes object in JSON representation to a file
    Args:
        my_obj (object): object to write
        filename (str): path to a file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
