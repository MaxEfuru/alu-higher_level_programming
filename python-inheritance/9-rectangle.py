#!/usr/bin/python3
""" import again """


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ inherit class """

    def __init__(self, width, height):
        """ still class """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ area """
        return (self.__width * self.__height)

    def __str__(self):
        """ area again """
        return ("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))
