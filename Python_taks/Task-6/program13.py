# Sherlock and the Valid String
# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

from collections import Counter

def isValid(s):
    freq = Counter(s)
    values = list(freq.values())
    
    # Count frequency of frequencies
    freq_count = Counter(values)
    
    if len(freq_count) == 1:
        # All characters occur the same number of times
        return "YES"
    elif len(freq_count) == 2:
        # Two different frequencies
        key1, key2 = freq_count.keys()
        # Case 1: One frequency occurs once and is 1 (remove that one character)
        if freq_count[key1] == 1 and key1 == 1:
            return "YES"
        if freq_count[key2] == 1 and key2 == 1:
            return "YES"
        # Case 2: One frequency occurs once and differs by 1 from the other
        if freq_count[key1] == 1 and key1 - key2 == 1:
            return "YES"
        if freq_count[key2] == 1 and key2 - key1 == 1:
            return "YES"
        return "NO"
    else:
        # More than two different frequencies
        return "NO"

