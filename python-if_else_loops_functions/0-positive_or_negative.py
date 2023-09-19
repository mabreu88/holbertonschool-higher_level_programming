#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number < 0:
    print('Is positive')
elif number == 0:
    print('is zero')
else:
    print('is negative')
