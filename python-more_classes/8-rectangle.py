#!/usr/bin/python3
""" a class that defines a rectangle """


class Rectangle:
    """ An empty class """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ __init__() function to assign values to object properties """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
                rect_str += str(self.print_symbol)

            if i != h - 1:
                rect_str += '\n'

        return rect_str

    def __str__(self):
        """ Return a string with printed Rectangle """

        return self.__print_rectangle()

    def __repr__(self):
        """ Returns the representation of the Rectangle """

        w = str(eval('self.width'))
        h = str(eval('self.height'))

        return 'Rectangle(' + w + ', ' + h + ')'

    def __del__(self):
        """ Print delete message """

        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Compare and returns the biggest rectangle based on the area  """
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError('rect_1 must be an instance of Rectangle')

        if isinstance(rect_2, Rectangle) is False:
            raise TypeError('rect_2 must be an instance of Rectangle')

        rct1_area = rect_1.area()
        rct2_area = rect_2.area()

        if rct1_area >= rct2_area:
            return rect_1
        return rect_2
