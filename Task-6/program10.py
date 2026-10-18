# Designer Door Mat
# https://www.hackerrank.com/challenges/designer-door-mat/problem


if __name__ == '__main__':
    N, M = map(int, input().split())

    # Top half
    for i in range(1, N, 2):
        pattern = ".|." * i
        print(pattern.center(M, "-"))

    # Middle line
    print("WELCOME".center(M, "-"))

    # Bottom half
    for i in range(N-2, 0, -2):
        pattern = ".|." * i
        print(pattern.center(M, "-"))
