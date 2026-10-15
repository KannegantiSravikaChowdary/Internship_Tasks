# Collections.Counter()
# https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

# Read input
n = int(input())  # number of shoes
shoe_sizes = list(map(int, input().split()))
shoe_counter = Counter(shoe_sizes)

customers = int(input())
earnings = 0

for _ in range(customers):
    size, price = map(int, input().split())
    if shoe_counter[size] > 0:   # shoe available
        earnings += price
        shoe_counter[size] -= 1  # decrement inventory

print(earnings)
