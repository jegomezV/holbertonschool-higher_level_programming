#!/usr/bin/python3
"""Ninth"""


def class_to_json(obj):
    """Serialize class attributes to dictionary
    Args:
        obj (object): object to be serialized
    """
    return (obj.__dict__)


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """__init__ method
        Args:
            first_name (str): first name
            last_name (str): last name
            age (int): age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Serializes object to dictionary"""
        return class_to_json(self)
