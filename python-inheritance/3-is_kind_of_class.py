#!/usr/bin/python3
""" Check if "obj" is an instance of the class """


def is_kind_of_class(obj, a_class):
    """ returns True if the object is an instance of, or if the object is an instance
   of a class that inherited from, the specified class ; otherwise False. """
    if not isinstance(obj, a_class):
        return False
    return True
