#!/usr/bin/env python3
def print_last_digit(number):
    num = str(number)
    num = num[-1]
    if number < 0:
        print(f"-{num}")
    else:
        print(num)
