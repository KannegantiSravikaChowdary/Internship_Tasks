# Separate the Numbers
# https://www.hackerrank.com/challenges/separate-the-numbers/problem

def separateNumbers(s):
    n = len(s)
    for length in range(1, n//2 + 1):
        first = int(s[:length])
        seq = str(first)
        next_num = first
        
        # Build the sequence until length of s
        while len(seq) < n:
            next_num += 1
            seq += str(next_num)
        
        # Check if it matches
        if seq == s:
            print("YES", first)
            return
    
    print("NO")
