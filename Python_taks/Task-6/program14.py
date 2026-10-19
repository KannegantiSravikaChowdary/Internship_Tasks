# Anagram
# https://www.hackerrank.com/challenges/anagram/problem

from collections import Counter
def anagram(s):
    # If length is odd, not possible
    if len(s) % 2 != 0:
        return -1
    
    mid = len(s) // 2
    s1 = s[:mid]
    s2 = s[mid:]
    
    # Count characters in both halves
    c1 = Counter(s1)
    c2 = Counter(s2)
    
    # Calculate how many characters in s1 are "extra"
    changes = 0
    for ch in c1:
        if c1[ch] > c2[ch]:
            changes += c1[ch] - c2[ch]
    
    return changes
