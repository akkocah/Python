def front_back(word):
    if len(word) == 1:
        return word
    else:
        return(word[-1] +word[1:-1] +word[0])

# def front_back(word):
#     list1 = list(word)
#     list1.insert(0,list1[-1])
#     list1.pop()
#     list1.insert(-1,list1[1])
#     list1.pop(1)
#     word = "".join(list1)
#     return word

# print(front_back('clarusway'))





