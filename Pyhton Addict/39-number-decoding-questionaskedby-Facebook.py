# QUESTION:
# This is an interview question asked by Facebook.
# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
# You can assume that the messages are decodable. For example, '001' is not allowed.

def num_encodings(s):
    if s.startswith('0'):
        return 0
    elif len(s) <= 1: 
        return 1
    total = 0
    if int(s[:2]) <= 26:
        total += num_encodings(s[2:])
    total += num_encodings(s[1:])
    return total

print(num_encodings("11"))