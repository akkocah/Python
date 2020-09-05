# QUESTION:
# This is an interview question asked by Airbnb.
# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5.
# [5, 1, 1, 5] should return 10, since we pick 5 and 5. (edited) 

def max_adj(arr):
    if not arr:
        return 0
    return max(max_adj(arr[1:]), arr[0] + max_adj(arr[2:]))

print(max_adj([2, 4, 6, 2, 5]))
print(max_adj([2, 4, 6, 2, 5,-1,1,100,21,56]))

def find(arr):
    first = 0
    second = 0
    for i in range(len(arr)):
        newsum = max(arr[i] + second, first)
        second = first
        first = newsum
    return first
print(max_adj([0,-1,-1,1]))
print(max_adj([2, 4, 6, 2, 5]))
print(find([2, 4, 6, 2, 5,-1,1,100,21,56]))