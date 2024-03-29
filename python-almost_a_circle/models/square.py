#!/usr/bin/python3
"""
class Square
"""
from .rectangle import Rectangle


class Square(Rectangle):
    """ square class """

    def __init__(self, size, x=0, y=0, id=None):
        """ class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ anathor attribute """
        attributes = "[Square] ({}) {}/{} - {}"
        return attributes.format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ Getter of the size attribute """
        return self.width

    @size.setter
    def size(self, value):
        """ setter for size """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ assign the  attributes """
        if len(args):
            i = 0
            keys_of_attributes = ['id', 'size', 'x', 'y']
            for value in args:
                if i < 4:
                    setattr(self, keys_of_attributes[i], value)
                    i += 1
        else:
            for keys_of_attributes, value in kwargs.items():
                setattr(self, keys_of_attributes, value)

    def to_dictionary(self):
        """ square dictionary """
        dic = {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
            }
        return dic
