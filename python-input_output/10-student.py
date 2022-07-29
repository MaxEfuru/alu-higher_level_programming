#!/usr/bin/python3
""" json to student """


class Student:
    """ first  student class """

    def __init__(self, first_name, last_name, age):
        """ first statement for the class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ function for converting """
        if type(attrs) is list and all([type(x) == str for x in attrs]):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__
