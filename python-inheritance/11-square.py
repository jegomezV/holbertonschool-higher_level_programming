#!/usr/bin/python3
"""Eleventh"""


class BaseGeometry:
    """BaseGeometry class with area method"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 1:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        return "[{}] {:d}/{:d}".format(
            type(self).__name__, self.__width, self.__height)

    def area(self):
        return self.__width * self.__height


class Square(Rectangle):
    """Square class"""
    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return "[{}] {:d}/{:d}".format(
            type(self).__name__, self.__size, self.__size)
