# Nested Lists
# https://www.hackerrank.com/challenges/nested-list/problem

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    
    # Extract all scores
    scores = sorted({s[1] for s in students})   # unique sorted scores
    second_lowest = scores[1]                   # pick the second lowest
    
    # Find all students with that score
    result = [s[0] for s in students if s[1] == second_lowest]
    
    # Print names alphabetically
    for name in sorted(result):
        print(name)
