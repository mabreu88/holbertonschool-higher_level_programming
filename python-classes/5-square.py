#!/usr/bin/python3
""" Square class
A square class
"""


class Square:
    """ Class define a square """

    def __init__(self, size=0):
        """
        __init__ Initializes the size value of the square.

        Attributes:
            size (:obj:`int`, optional): The size of the square.

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

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        """__init__

        The size setter method update the size value of the square.

        Attributes:
            size (:obj:`int`): The new size of the square.

        Raises:
            TypeError: If `size` type is not `int`.

            ValueError: If `size` is less than `0`.

        """

        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """ Return the square area """
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
            return None

        for i in range(1, self.area() + 1):
            print('#', end='')

            if i % self.__size == 0 and i > 0:
                print()
