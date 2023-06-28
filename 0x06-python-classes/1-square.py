#!/usr/bin/python3
"""Square class definition"""


class Square:
  """
    This class represents a square.

    Attributes:
        __size (int): The size of the square.
    """
    def __init__(self, size):
        """Initializes a new instance of the Square Class.
        Args:
            size (int):The  size of a side of the square
        Returns: None
        """
        self.__size = size
