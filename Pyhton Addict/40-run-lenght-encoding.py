# QUESTION:
# This is an interview question asked by Amazon.
# Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character.
# For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".
# Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.

def lengthencode(data):
    result = ""
    prev_char = ""
    count = 1
    for i in data:
        if i != prev_char:
            if prev_char:
                result += str(count) + prev_char
            count = 1
            prev_char = i
        else:
            count +=1
    result += str(count) + prev_char
    return result
#############################################

def decode(s):
    result = ""
    count = 0
    for i in s:
        if i.isdigit():
            count = count*10 + int(i)
        else:
            result += count * i
            count = 0
    return result 
##################################################
def encode2(s):
    result = s[0]
    count = 1
    for i in range(1,len(s)):
        if s[i] != result[-1]:
            result = result[:-1]+str(count)+result[-1]+s[i]
            count = 1
        else:
            count += 1
    result = result[:-1]+str(count)+result[-1]
    return result
##############################################
def encode(s):
    chars = [s[0]]
    numbers = [0]
    for item in s:
        if item != chars[-1]:
            chars.append(item)
            numbers.append(1)
        else:
            numbers[-1] += 1
    return "".join([str(i)+j for i,j in zip(numbers,chars)])
# print(lengthencode("AAAABBBCCDAA"))

# def decode(lst):
#     decoded = ""    
#     for i in range(0, len(lst),2):
#         decoded += (int(lst[i])*lst[i+1]) 
#     return(decoded)
    
# print(decode("4A3B2C1D2A"))

