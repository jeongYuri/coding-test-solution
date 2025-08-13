import sys
input = sys.stdin.readline

n,m = map(int,input().split())
array_a = [list(map(int, input().split())) for _ in range(n)]
array_b = [list(map(int, input().split())) for _ in range(n)]

res = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(array_a[i][j]+array_b[i][j])
    res.append(row)

for r in res:
    print(*r)
