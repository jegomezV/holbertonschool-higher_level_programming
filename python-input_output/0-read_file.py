#!/usr/bin/python3
"""Zero"""


def read_file(filename=""):
    """Read file and print lines
    Args:
        filename (str): string of path to file
    """
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')
