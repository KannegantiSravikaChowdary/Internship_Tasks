# Gemstones
# https://www.hackerrank.com/challenges/gem-stones/problem

def gemstones(arr):
    sets = [set(rock) for rock in arr]
    common = set.intersection(*sets)
    return len(common)
