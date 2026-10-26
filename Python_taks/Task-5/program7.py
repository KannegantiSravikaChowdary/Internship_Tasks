# Symmetric Difference
# https://www.hackerrank.com/challenges/symmetric-difference/problem

if __name__ == "__main__":
    # Read input
    m = int(input())
    set_a = set(map(int, input().split()))
    n = int(input())
    set_b = set(map(int, input().split()))
    
    # Symmetric difference
    result = sorted(set_a ^ set_b)   # ^ operator gives symmetric difference
    
    # Print each element on a new line
    for num in result:
        print(num)
