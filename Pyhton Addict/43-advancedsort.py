# Advanced List Sort
# https://edabit.com/challenge/6vSZmN66xhMRDX8YT
# Create a function that takes a list of numbers or strings and 
# returns a list with the items from the original list stored 
# into sublists. Items of the same value should be in the same sublist
# advanced_sort([2, 1, 2, 1]) ➞ [[2, 2], [1, 1]]
# advanced_sort([5, 4, 5, 5, 4, 3]) ➞ [[5, 5, 5], [4, 4], [3]]

def advanced_sort(lst):
	return [[i] * lst.count(i) for i in sorted(set(lst), key=lst.index)]

a = advanced_sort([5, 4, 5, 5, 4, 3])
print(a)

def advanced_sort(liste): 
    son=[]
    while len(liste)>0:
        i = liste[0]
        temp=[]
        while i in liste:
            temp.append(i)
            liste.remove(i)
        son.append(temp)
    return (son) 

def advanced_sort(lst):
  return [[i] * lst.count(i) for i in sorted(set(lst), key=lambda i :lst.index(i))]

def advanced_sort ( lst ) :
    return [[i]*lst.count(i) for i in dict.fromkeys(lst)]