#!/usr/bin/python3#!/usr/bin/python3
"""Script to create class Square"""


class Square:
    """Class Square"""
    def __init__(self, size=0):
        """Conditionals"""
        self.__size = size
        if type(size) is not int:
            raise ValueError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
    @property
    def size(self):
        return self.__size
    
    @property.setter
    def size(self, value):
        self.__size = value

    def area(self):
        """Define square area"""
        return self.__size**2
