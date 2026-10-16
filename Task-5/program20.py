# Piling Up!
# https://www.hackerrank.com/challenges/piling-up/problem

from collections import deque

def can_stack(cubes):
    cubes = deque(cubes)
    last = float('inf')
    while cubes:
        if cubes[0] >= cubes[-1]:
            pick = cubes.popleft()
        else:
            pick = cubes.pop()
        if pick > last:
            return "No"
        last = pick
    return "Yes"

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        cubes = list(map(int, input().split()))
        print(can_stack(cubes))
