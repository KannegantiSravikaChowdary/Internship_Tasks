# Pangrams
# https://www.hackerrank.com/challenges/pangrams/problem

def pangrams(s):
    letters = set(s.lower())
    # Check if all 26 letters are present
    if set("abcdefghijklmnopqrstuvwxyz").issubset(letters):
        return "pangram"
    else:
        return "not pangram"
