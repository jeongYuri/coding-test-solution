import sys
input = sys.stdin.readline

n = int(input())
if n<4:
    res = 0
else:
    res = (n * (n - 1) * (n - 2) * (n - 3)) // 24
print(res)