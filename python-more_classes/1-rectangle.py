#!/usr/bin/python3
"""Script to create a Rectangle class"""


class Rectangle:
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        self.width = width
    @property
    def width(self):
        """Return the width to the rectangle"""
        return self._width
    @width.setter
    def width(self, value):
        """set the self.__size to value, the value must be a
        integer and >= 0"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self._width = value

    @property
    def height(self):
        """Return the height to the rectangle"""
        return self._height
    @height.setter
    def height(self, value):
        """set the self.__height to value, the value must be a
        integer and >= 0"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self._height = value
