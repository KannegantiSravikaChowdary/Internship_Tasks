# Beautiful Binary String
# https://www.hackerrank.com/challenges/beautiful-binary-string/problem

def beautifulBinaryString(b):
    count = 0
    i = 0
    while i <= len(b) - 3:
        if b[i:i+3] == "010":
            count += 1
            # Skip ahead by 3 to avoid overlapping fixes
            i += 3
        else:
            i += 1
