# CamelCase
# https://www.hackerrank.com/challenges/camelcase/problem

def camelcase(s):
    # Write your code here
     return 1 + sum(1 for c in s if c.isupper())
