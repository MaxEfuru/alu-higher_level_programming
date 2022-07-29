#!/usr/bin/python3
""" My list """


class MyList(list):
    """ print the list """

    def print_sorted(self):
        """ function for list print """
        print(sorted(self))
