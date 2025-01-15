import sys

input = sys.stdin.readline
n, m = map(int, input().split())

pascal = [[0] * (i + 1) for i in range(n)]

for i in range(n):
    pascal[i][0] = 1
    pascal[i][-1] = 1

for i in range(2, n):
    for j in range(1, i):
        pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]

print(pascal[n - 1][m - 1])