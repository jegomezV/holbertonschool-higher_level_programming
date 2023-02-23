#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    check_m = []
    for i in range(len(my_list)):
        if (my_list[i] % 2 == 0):
            check_m.append(True)
        else:
        check_m.append(False)
    return check_m
