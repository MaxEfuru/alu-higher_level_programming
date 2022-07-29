#!/usr/bin/python3
""" json to save file """
import json
""" save and write module """


def save_to_json_file(my_obj, filename):
    """ function to put to json and write as well """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
