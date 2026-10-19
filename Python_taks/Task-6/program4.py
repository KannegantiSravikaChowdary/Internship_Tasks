# Funny String
# https://www.hackerrank.com/challenges/funny-string/problem

def funnyString(s):
    # Write your code here
    rev = s[::-1]
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(rev[i]) - ord(rev[i-1])):
            return "Not Funny"
    return "Funny"
