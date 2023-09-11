#!/usr/bin/python3
"""Exact same object function"""


def is_same_class(obj, a_class):
    """function: is_same_class
    obj: an object
    a_class: a class
    Returns: Boolean expression
    """
    return type(obj) == a_class
