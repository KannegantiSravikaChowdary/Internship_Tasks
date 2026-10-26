# Find the Runner-Up Score!
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr=list(arr)
    largest=max(arr)
    second_largest=float('-inf')
    for i in arr:
        if i>second_largest and i!=largest:
            second_largest=i 
    print(second_largest)
