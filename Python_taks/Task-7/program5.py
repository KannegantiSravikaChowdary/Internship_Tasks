# Alternating Characters
# https://www.hackerrank.com/challenges/alternating-characters/problem

def alternatingCharacters(s):
    # Write your code here
    deletions = 0
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            deletions += 1
    return deletions
