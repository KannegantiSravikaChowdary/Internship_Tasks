# Mutations
# https://www.hackerrank.com/challenges/python-mutations/problem

def mutate_string(string, position, character):
    s=list(string)
    s[position]=character
    a="".join(s)
    return a
