#daily-python-challenge
# QUESTION:
# This is an interview question asked by Google.
# Given an integer n and a list of integers, write a function that randomly generates a number from 0 to n-1 that isn't in that given integer list.

import numpy as np
import random

lst = [1,6,9,10]
def rand_num(lst, n):
    b = int("".join(map(str, (random.sample(range(0,n),1)))))
    if b not in lst:
        return b
    else:
        return rand_num(lst, n)
print(rand_num(lst, 5))

##############################################

lst = [1,6,9,10]
def rand_int(lst, n):
    a=int(np.random.choice(range(0,n), 1))
    return a if a not in lst else rand_int(lst, n)

print(rand_int(lst, 5))