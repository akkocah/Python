# QUESTION:
# This is an interview question asked by Google.
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

lst = [10, 15, 3, 7]
def two_sum(lst, k):
    seen = set()
    for num in lst:
        if k - num in seen:
            return True
        seen.add(num)
    return False
    
print(two_sum(lst, 20))

k = 17
y=[x for x in lst for i in lst if x!=i and x+i==k]
print(y)
print(bool(y))