#!/usr/bin/python3
""" Function that return a list of attributes and methods of an object """


def lookup(obj):
    """ returns the list of available attributes and methods of an object """
    return dir(obj)
