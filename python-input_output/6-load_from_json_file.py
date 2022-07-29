#!/usr/bin/python3
""" json module for reading """
import json
""" do both reading and loading """


def load_from_json_file(filename):
    """ load json and read as well """
    with open(filename, "r", encoding="utf-8") as f:
        return json.loads(f.read())
