# Game of Thrones - I
# https://www.hackerrank.com/challenges/game-of-thrones/problem

def gameOfThrones(s):
    freq = Counter(s)
    
    # Count how many characters have odd frequency
    odd_count = sum(1 for v in freq.values() if v % 2 != 0)
    
    # Valid if at most one odd frequency
    return "YES" if odd_count <= 1 else "NO"
