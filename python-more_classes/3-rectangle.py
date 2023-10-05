#!/usr/bin/python3
""" a class that defines a rectangle """


class Rectangle:
    """ An empty class """

    def __init__(self, width=0, height=0):
        """ __init__() function to assign values to object properties """

        self.width = width
        self.height = height

    @property
    def height(self):
        """ Returns the height of the Rectangle """
        return self.__height

    @property
    def width(self):
        """ Returns the width of the Rectangle """
        return self.__width

    @height.setter
    def height(self, value):
        """ Checks the parameters and set the size of the Rectangle """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @width.setter
    def width(self, value):
        """ Checks the parameters and set the size of the Rectangle """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        """ Return the area of the Rectangle """
        return self.__height * self.__width

    def perimeter(self):
        """ Return the perimeter of the Rectangle """
        if self.__height == 0 or self.__width == 0:
            return 0
        return self.__height * 2 + self.__width * 2

    def __print_rectangle(self):
        """ print the Rectangle with their size """

        rect_str = ''
        w = self.__width
        h = self.__height

        if w == 0 or h == 0:
            return rect_str

        for i in range(h):
            for j in range(w):
                rect_str += '#'

            if i != h - 1:
                rect_str += '\n'

        return rect_str

    def __str__(self):
        """ Return a string with printed Rectangle """

        return self.__print_rectangle()
