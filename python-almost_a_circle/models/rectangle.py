#!/usr/bin/python3
"""the class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Definition of the class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """__init__ method of rectangle class args:"""
        super().__init__(id)
        self.height = height
        self.width = width
        self.x = x
        self.y = y

    @property
    def heigh(self):
        return self.__heigh

    @heigh.setter
    def heigh(self, value):
        self.__heigh = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
