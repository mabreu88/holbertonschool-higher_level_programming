#!/usr/bin/python3
""" Check if "obj" is an instance of the class """


def is_kind_of_class(obj, a_class):
    """ eturns True if the object is an instance of, or if the object is an instance \n
    of a class that inherited from, the specified class ; otherwise False. """
    if type(obj) == a_class:
        return True
    return False
