#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """ This is a Square Class """
    def __init__(self, size=0):
        """ check if size is int.
        Args:
            size: size of the square (1 side).
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        """ returns size variable of Square class instance """
        return self.__size

    @size.setter
    def size(self, value):
        """ sets size variable of Square class instance """
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
