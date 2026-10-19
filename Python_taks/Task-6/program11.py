# Two Strings
# https://www.hackerrank.com/challenges/two-strings/problem

def twoStrings(s1, s2):
    # Write your code here
    set1 = set(s1)
    set2 = set(s2)
    
    if set1 & set2:
        return "YES"
    else:
        return "NO"
