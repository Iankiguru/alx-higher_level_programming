#!/usr/bin/python3
""" defines a class square """


class Square:
    """ square with private instance attribute __size """

    def __init__(self, size=0):
        """
        this class initializes square
        Args:
            size: the size of side of square
        """

        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """
        finds the area of a square
        Returns:
            the area of the square
        """

        return self.__size ** 2
