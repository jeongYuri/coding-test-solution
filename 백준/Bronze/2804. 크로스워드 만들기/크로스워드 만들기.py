import sys
input = sys.stdin.readline

a, b = input().split()
n = len(a)
m = len(b)

for i in range(n):
    if a[i] in b:
        col = i
        row = b.index(a[i])
        break
for i in range(m):
    if i== row:
        print(a)
    else:
        print('.' * col + b[i] + '.'*(len(a)-col-1))