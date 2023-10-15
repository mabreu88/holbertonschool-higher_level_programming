#!/usr/bin/python3
from json import dumps
""" function that returns the JSON representation of an object (string) """


def to_json_string(my_obj):
    """ returns the JSON representation of an object """
    return dumps(my_obj)
