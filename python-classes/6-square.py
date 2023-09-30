#!/usr/bin/python3
""" Square class
A square class
"""


class Square:
    """ Class define a square """

    def __init__(self, size=0, position=(0, 0)):
        """
        __init__ Initializes the size and position values of the square.

        Attributes:
            size (:obj:`int`, optional): The size of the square.
            position (:obj:`tuple`, optional): The position of the square.

        Raises:
            TypeError: size must be an integer, otherwise raise a TypeError
            ValueError: if size is less than 0, raise a ValueError
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

        if not isinstance(position, tuple) or len(position) != 2 or \
           not all(isinstance(i, int) for i in position) or \
           not all(i >= 0 for i in position):
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = position  # Mantén el nombre como __position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, size):
        """__init__

        The size setter method update the size value of the square.

        Attributes:
            size (:obj:`int`, optional): The size of the square.

        Raises:
            TypeError: size must be an integer, otherwise raise a TypeError
            ValueError: if size is less than 0, raise a ValueError

        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    @position.setter
    def position(self, position):
        if not isinstance(position, tuple) or len(position) != 2 or \
           not all(isinstance(i, int) for i in position) or \
           not all(i >= 0 for i in position):
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = position

    def area(self):
        """ Return the square area """
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
            return None

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(' ' * self.__position[0] + '#' * self.__size)
