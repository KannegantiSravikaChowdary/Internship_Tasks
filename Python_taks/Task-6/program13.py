# Set .union() Operation
# https://www.hackerrank.com/challenges/py-set-union/problem

if __name__ == '__main__':
    n_eng = int(input())
    eng = set(map(int, input().split()))
    n_fre = int(input())
    fre = set(map(int, input().split()))
    result = eng.union(fre)

 
    print(len(result))
