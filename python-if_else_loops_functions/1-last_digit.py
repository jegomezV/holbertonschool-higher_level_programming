#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    lastnum = number % -10
    print(f"Last digit of {number} is {lastnum} and is less than 6 and not 0")

if number >= 0:
    lastnum = number % 10
    if number > 5:
        print(f"Last digit of {number} is {lastnum} and is greater than 5")
    elif number == 0:
        print(f"Last digit of {number} is {lastnum} and is 0")
