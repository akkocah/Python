# This is an interview question asked by Stripe.
# Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
# You can modify the input array in-place.

def find_missing(array):
   array = sorted(array)
   array_pos = [i for i in array if i>=0]
   print(array_pos)
   control = list(range(array_pos[0], array_pos[-1]+1))
   return array_pos[-1] +1 if control == array_pos else list(set(control).difference(array_pos))[0]
print(find_missing([3,6,-1,1]))

###########################################################

def x(ls):
    srtd = sorted([i for i in ls if i >= 0])
    return [i+1 for i in srtd if i+1 not in srtd][0]
print(x([3,6,-1,1]))

###########################################################

def missing_num(lst):
    srt = []
    for i in lst:
        if i >=0: srt.append(i)
    srt = sorted(srt)
    result = []
    for i in srt:
        if i+1 not in srt:result.append(i+1)
    return result[0]
print(missing_num([3,6,-1,1,2]))

def check(my_array):
    for i in range(max(my_array)+2):
        if i>0 and not i in my_array:
            return i 
print(check([6,-1,1,2]))