#!/usr/bin/python3
"""first class Base"""


class Base:
    """Definition of the class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Definition of the method init"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
