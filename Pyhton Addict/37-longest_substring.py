# QUESTION:
# This is an interview question asked by Amazon.
# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
def longest(s, k):
    return sorted([s[i:j] for i in range(len(s)) for j in range(
        i + 1, len(s) + 1) if len(set(list(s[i:j]))) <= k], key=len)[-1]

print(longest("abcba",2))

###########################################

def longest_substr(s, k):
    current_longest = ''
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if len(set(substring)) <= k and len(substring) > len(current_longest):
                current_longest = substring
    return len(current_longest), current_longest

print(longest_substr("abcba",2))