import sys
input = sys.stdin.readline

def is_valid(prev, curr, op):
    if op == '<':
        return prev < curr
    else:
        return prev > curr

def backtrack(depth, path):
    if depth == k + 1:  
        results.append(path)
        return

    for num in range(10):
        if not visited[num]:
            if depth == 0 or is_valid(int(path[-1]), num, ops[depth - 1]):
                visited[num] = True
                backtrack(depth + 1, path + str(num))
                visited[num] = False

k = int(input())
ops = input().split()

visited = [False] * 10
results = []

backtrack(0, "")
results.sort()
print(results[-1])
print(results[0])
