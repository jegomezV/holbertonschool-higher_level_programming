#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_d = str(number)
last_d = int(last_d[-1])
if number < 0:
    print(f"Last digit of {number} is -{last_d} and is less than 6 and not 0")
elif last_d > 5:
    print(f"Last digit of {number} is {last_d} and is greater than 5")
elif last_d == 0:
    print(f"Last digit of {number} is {last_d} and is 0")
