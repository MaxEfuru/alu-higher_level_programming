#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for i in range(x):
        try:
            print(my_list[i], end="")
            if i == x - 1:
                print("")
        except IndexError:
            print("")
            break
    if x >= len(my_list):
        return len(my_list)
    return x
