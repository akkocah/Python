def missing_char(word, n):
    
    word = word.replace(word[n], "")
    return word
    
print(missing_char('kitchen', 4))

def missing_char1(word, n):
    word = word[:n] + word[n+1:]
    #word = word.replace(word[n], "")
    return word
    
print(missing_char1('kitchen', 4))


# >>> s = 'abcd'
# >>> def remove(s, indx):
#         return ''.join(x for x in s if s.index(x) != indx)

# >>> remove(s, 1)
# 'acd'



# You can bypass all the list operations with slicing:

# S = S[:1] + S[2:]

# or more generally

# S = S[:Index] + S[Index + 1:]

a = "ali okula git"
a = a[:5] + a[7:]
print(a)

