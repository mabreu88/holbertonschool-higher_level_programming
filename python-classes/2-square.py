#!/usr/bin/python3
""" Square class
A square class
"""


class Square:
    """ Class define a square """

    def __init__(self, size=0):
        """__init__
        __init__ Initializes the size value of the square.

        Attributes:
            size (:obj: 'int', optional): The square size

        Raises: 
        TypeError: size must be an integer, otherwise raise a TypeError

        ValueError: if size is less than 0, raise a ValueError
          """
        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
