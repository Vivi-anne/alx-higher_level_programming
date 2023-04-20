#!/usr/bin/python3
"""Defines a square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializing new Square.

        Args:
            size (int): size of the new Square.
            x (int): x coordinate of the new Square.
            y (int): y coordinate of the new Square.
            id (int):identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updating the Square.

        Args:
            *args (ints): New attribute values.
                - 1st arg represents id attribute
                - 2nd arg represents size attribute
                - 3rd arg represents x attribute
                - 4th arg represents y attribute
            **kwargs (dict): New value pairs of attributes.
        """
        if args and len(args) != 0:
            l = 0
            for arg in args:
                if l == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif l == 1:
                    self.size = arg
                elif l == 2:
                    self.x = arg
                elif l == 3:
                    self.y = arg
                l += 1

        elif kwargs and len(kwargs) != 0:
            for a, b in kwargs.items():
                if a == "id":
                    if b is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = b
                elif a == "size":
                    self.size = b
                elif a == "x":
                    self.x = b
                elif a == "y":
                    self.y = b

    def to_dictionary(self):
        """Return  dict representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print()/ str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
