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
