# QUESTION:
# This is an interview question asked by Microsoft.
# Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found in the matrix by going left-to-right, or up-to-down.
# For example, given the following matrix:
# [['F', 'A', 'C', 'I'],
#  ['O', 'B', 'Q', 'P'],
#  ['A', 'N', 'O', 'B'],
#  ['M', 'A', 'S', 'S']]
# and the target word 'FOAM', you should return true, since it's the leftmost column. Similarly, given the target word 'MASS', you should return true, since it's the last row.

table=[['F', 'A', 'C', 'I'],
    ['O', 'B', 'Q', 'P'],
    ['A', 'N', 'O', 'B'],
    ['M', 'A', 'S', 'S']]

def find_word(table, word):
    for i in range(len(table)):
        for j in range(len(table[0])):
            if "".join(table[i][j:len(word)]) == word: 
                return True # horizantal control
            if ''.join([table[x][j] for x in range(i, min(len(table), len(word)))]) == word:
                return True # vertical control
    return False
print(find_word(table, "FOAM"))