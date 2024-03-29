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
    def height(self):
        """Rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """Show representation of rectangle"""
        for y in range(self.__y):
            print()
        for columns in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for rows in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """String function"""
        return ("[{}] ({}) {}/{} - {}/{}".format(type(self).__name__, self.id,
                self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """Adding the public method"""
        if len(args) > 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.width = arg
                if i == 2:
                    self.height = arg
                if i == 3:
                    self.x = arg
                if i == 4:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
