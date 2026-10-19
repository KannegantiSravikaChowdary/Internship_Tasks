# Super Reduced String
# https://www.hackerrank.com/challenges/reduced-string/problem

def superReducedString(s):
    # Write your code here
    stack = []
    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()  # remove adjacent pair
        else:
            stack.append(ch)
    
    return "".join(stack) if stack else "Empty String"
