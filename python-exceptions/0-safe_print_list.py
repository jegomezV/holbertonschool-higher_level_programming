#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for index in range(x):
            print("{}".format(my_list[index]))
        print()
        return x
    except (TypeError, IndexError):
        print()
        return index
