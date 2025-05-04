import sys
input = sys.stdin.readline
def dfs(idx, result, add, sub, mul, div):
    global min_value, max_value
    if idx==n:
        min_value = min(min_value, result)
        max_value = max(max_value, result)
        return
    if add > 0:
        dfs(idx + 1, result + numbers[idx], add - 1, sub, mul, div)
    if sub > 0:
        dfs(idx + 1, result - numbers[idx], add, sub - 1, mul, div)
    if mul > 0:
        dfs(idx + 1, result * numbers[idx], add, sub, mul - 1, div)
    if div > 0:
        if result < 0:
            dfs(idx + 1, -(-result // numbers[idx]), add, sub, mul, div - 1)
        else:
            dfs(idx + 1, result // numbers[idx], add, sub, mul, div - 1)


n = int(input())
numbers = list(map(int,input().split()))
plus, minus, multiply, divide = map(int, input().split())

min_value = float('inf')
max_value = float('-inf')

dfs(1,numbers[0],plus,minus, multiply, divide)
print(max_value)
print(min_value)

