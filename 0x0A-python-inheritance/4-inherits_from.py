#!/usr/bin/python3
"""Module: only subclass of"""


def inherits_from(obj, a_class):
    """A function that returns True if the object is an instance of a class that inherited (directly or indirectly)"""
    return type(obj) != a_class and isinstance(obj, a_class)
