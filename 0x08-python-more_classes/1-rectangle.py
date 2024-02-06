#!/usr/bin/python3
"""Define a class Rectangle."""


class Rectangle:
    """A class representing a Rectangle."""
    def __init__(self, width=0, height=0):

        """
        Initialisze the Rectangle object.

        Parameters:
            width, height (int): of the rectangle.

        Raises:
            TypeError: Parameters are not int.
            ValueError: Parameters are less than 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width attribute."""
        return self.__width

    @width.setter
    def width(self, width):
        """Set the width attribute."""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >=0")
        self.__width = width

    @property
    def height(self):
        """retrieve the height attribute."""
        return self.__height

    @height.setter
    def height(self, height):
        """set de height attribute """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >=0")
        self.__height = height
