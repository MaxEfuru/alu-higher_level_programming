#!/usr/bin/python3
""" inherits  """


def inherits_from(obj, a_class):
    """ check if it inherits from the class """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
