# Word Order
# https://www.hackerrank.com/challenges/word-order/problem

from collections import OrderedDict

if __name__ == '__main__':
    n = int(input())
    word_count = OrderedDict()
    
    for _ in range(n):
        word = input().strip()
        word_count[word] = word_count.get(word, 0) + 1
    
    # Print number of distinct words
    print(len(word_count))
    
    # Print occurrences in order of appearance
    print(' '.join(map(str, word_count.values())))
