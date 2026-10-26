# Set .intersection() Operation
# https://www.hackerrank.com/challenges/py-set-intersection-operation/problem

if __name__ == '__main__':
    n_eng = int(input())
    eng = set(map(int, input().split()))
    n_fre = int(input())
    fre = set(map(int, input().split()))

    # Intersection of both sets
    result = eng.intersection(fre)

    # Print the total number of students with both subscriptions
    print(len(result))
