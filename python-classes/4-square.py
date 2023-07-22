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
        """Return size of square"""
        return self.__size
    
    @size.setter
    def size(self, value):
        """set the self.__size to value, the value must be a
        integer and >= 0"""

        self.__size = value
        if type(value) is not int:
            raise ValueError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Define square area"""
        return self.__size**2
