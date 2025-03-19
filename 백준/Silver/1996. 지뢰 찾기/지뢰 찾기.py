import sys
input = sys.stdin.readline

n = int(input())
map_data = [list(input().strip()) for _ in range(n)]
res = [[0] * n for _ in range(n)]
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
for i in range(n):
    for j in range(n):
        if map_data[i][j] != '.':
            res[i][j]='*'
            num = int(map_data[i][j])

            for d in range(8):
                ni,nj = i+dx[d],j+dy[d]
                if 0<=ni < n and 0<=nj<n and res[ni][nj]!='*':
                    res[ni][nj] += num
for i in range(n):
    for j in range(n):
        if isinstance(res[i][j], int):
            if res[i][j] >= 10:
                res[i][j] = 'M'  
            else:
                res[i][j] = str(res[i][j])

for row in res:
    print("".join(str(cell) for cell in row))
