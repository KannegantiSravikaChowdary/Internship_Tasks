# Check Subset
# https://www.hackerrank.com/challenges/py-check-subset/problem

if __name__ == '__main__':
    t = int(input()) 
    for _ in range(t):
        n_a = int(input())
        A = set(map(int, input().split()))
        n_b = int(input())
        B = set(map(int, input().split()))
        

        print(A.issubset(B))
