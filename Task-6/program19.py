# 19
# Company Logo
# https://www.hackerrank.com/challenges/most-commons/problem

from collections import Counter

if __name__ == '__main__':
    s = input()
    counts = Counter(s)
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

    for char, freq in sorted_counts[:3]:
        print(char, freq)
