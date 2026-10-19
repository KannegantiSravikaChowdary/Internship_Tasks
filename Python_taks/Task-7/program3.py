# Mars Exploration
# https://www.hackerrank.com/challenges/mars-exploration/problem

def marsExploration(s):
    # Write your code here
    expected = "SOS"
    changes = 0
    
    for i in range(len(s)):
        if s[i] != expected[i % 3]:
            changes += 1
    
    return changes
