#!/usr/bin/python3
"""Defines an empty class Rectangle that defines a rectangle """


class Rectangle:
    """Represents a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

        @property
        def width(self):
            """get/set the width of the rectangle"""
            return self._width

        @width.setter
        def width(self, value):
        """
            Checking for TypeError and ValueError and sets up the private var
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

        @property
        def width(self):
            """get/set the height of the rectangle"""
            return self._height

        @height.setter
        def height(self, value):
        """
            Checking for TypeError and ValueError and sets up the private var
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
