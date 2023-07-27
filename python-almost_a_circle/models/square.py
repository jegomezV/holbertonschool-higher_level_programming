#!/usr/bin/python3
"""Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Define Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """__init__ method"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """String function"""
        name = str(self.__class__.__name__)
        id = str(self.id)
        size = str(self.width)
        x = str(self.x)
        y = str(self.y)
        return ("[{}] ({}) {}/{} - {}".format(name, id,
                x, y, size))
