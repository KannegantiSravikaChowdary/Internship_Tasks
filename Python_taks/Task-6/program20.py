# Validating the Phone Number
# https://www.hackerrank.com/challenges/validating-the-phone-number/problem

import re

if __name__ == '__main__':
    n = int(input())  
    pattern = re.compile(r'^[789]\d{9}$')  # regex: starts with 7/8/9, followed by 9 digits
    
    for _ in range(n):
        s = input().strip()
        if pattern.match(s):
            print("YES")
        else:
            print("NO")
