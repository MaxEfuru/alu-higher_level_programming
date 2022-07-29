#!/usr/bin/python3
""" Read this file only """


def read_file(filename=""):
    """ Open and read as well """
    with open(filename, encoding="utf-8") as readfile:
        print(readfile.read(), end='')
