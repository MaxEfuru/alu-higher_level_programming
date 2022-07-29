#!/usr/bin/python3
""" Write inside the file """


def write_file(filename="", text=""):
    """ Do both reading and counting """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    return len(text)
