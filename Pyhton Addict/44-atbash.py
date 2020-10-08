# Atbash Cipher
# https://edabit.com/challenge/MGALfBAXhXqqdFyqo
# The Atbash cipher is an encryption method in which each letter 
# of a word is replaced with its "mirror" letter in the alphabet: 
# A <=> Z; B <=> Y; C <=> X; etc.
# Create a function that takes a string and applies the Atbash cipher to it.

#############1.cozum###############

def atbash(txt):
    l_case = list(map(chr, range(ord("a"), ord("z") + 1)))  # veya normal harflerle de liste belirlenebilir.
    u_case = list(map(chr, range(ord("A"), ord("Z") + 1)))
    t_case = u_case + l_case
    r_case = u_case[::-1] + l_case[::-1]
    return "".join(r_case[t_case.index(ch)] if ch.isalpha() else ch for ch in txt)

#############2.solution###############
ul = "".join([chr(i) for i in range(65,91)])    #ABCDEFGHIJKLMNOPQRSTUVWXYZ
ll =  "".join([chr(i) for i in range(97,123)])  #abcdefghijklmnopqrstuvwxyz
def atbash(s):
    return "".join([(i.isupper()*ul[-(ul.find(i)+1)] or i.islower()*ll[-(ll.find(i)+1)] or i ) for i in s])

#############3.solution###############
def atbash ( txt ) :
    ch= ''.join([ chr(65+i) for i in range(58) ]) # ascii kodu 65'ten 123e karakterlerin stringi oluşturur
    return ''.join([ch[::-1] [ch.index(i)] if i.isalpha() else i for i in txt]).swapcase()

#############4.solution###############
def atbash(B):
	A="abcdefghijklmnopqrstuvwxyz"
	D, C="ABCDEFGHIJKLMNOPQRSTUVWXYZ", ""
	for i in B:
		if i in A: C+=A[-(A.index(i)+1)]
		elif i in D: C+=D[-(D.index(i)+1)]
		else: C+=i
	return C