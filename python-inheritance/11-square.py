#!/usr/bin/python3
"""Defines a Square class that inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size (width and height) of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Return the string representation of the Square."""
        return "[Square] {}/{}".format(self._Rectangle__width,
                                        self._Rectangle__height)
