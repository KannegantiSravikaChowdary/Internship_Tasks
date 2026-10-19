# Making Anagrams
# https://www.hackerrank.com/challenges/making-anagrams/problem
from collections import Counter
    c1 = Counter(s1)
    c2 = Counter(s2)
    
    deletions = 0
    all_chars = set(c1.keys()) | set(c2.keys())
    for ch in all_chars:
        deletions += abs(c1[ch] - c2[ch])
    
    return deletions
