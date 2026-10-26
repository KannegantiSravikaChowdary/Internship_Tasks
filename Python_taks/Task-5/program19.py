# Merge the Tools!
# https://www.hackerrank.com/challenges/merge-the-tools/problem

def merge_the_tools(string, k):
    # your code goes here
    s=string
    for i in range(0, len(s), k):
        substring = s[i:i+k]
        result = ""
        for c in substring:
            if c not in result:
                result += c
        print(result)
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
