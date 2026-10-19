# Weighted Uniform Strings
# https://www.hackerrank.com/challenges/weighted-uniform-string/problem

def weightedUniformStrings(s, queries):
weights = set()
    prev_char = ''
    current_count = 0
    
    for ch in s:
        weight = ord(ch) - ord('a') + 1
        if ch == prev_char:
            current_count += 1
        else:
            current_count = 1
            prev_char = ch
        # Add all possible uniform substring weights ending here
        weights.add(weight * current_count)
    
    # Answer queries
    return ["Yes" if q in weights else "No" for q in queries]
