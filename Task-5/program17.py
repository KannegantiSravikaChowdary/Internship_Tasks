# No Idea!
# https://www.hackerrank.com/challenges/no-idea/problem

n, m = map(int, input().split())        # n = array length, m = set size
arr = list(map(int, input().split()))   # the array
A = set(map(int, input().split()))      # set A
B = set(map(int, input().split()))      # set B

happiness = 0
for num in arr:
    if num in A:
        happiness += 1
    elif num in B:
        happiness -= 1

print(happiness)

