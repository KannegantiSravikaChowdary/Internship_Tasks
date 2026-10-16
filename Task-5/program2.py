# String Split and Join
# https://www.hackerrank.com/challenges/python-string-split-and-join/problem

def split_and_join(line):
    # write your code here
    a=line.split(" ")
    result="-".join(a)
    return result
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
