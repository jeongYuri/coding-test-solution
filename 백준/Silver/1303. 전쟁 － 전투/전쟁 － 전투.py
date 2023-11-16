import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
field = [list(input().strip()) for _ in range(m)]

def bfs(y, x, wb):
    count = 0
    check[y][x] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= ny < m and 0 <= nx < n:
            if field[ny][nx] == wb and check[ny][nx] == 0:
                count += bfs(ny, nx, wb)
    return count + 1

check = [[0] * n for _ in range(m)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
w, b = 0, 0

for i in range(m):
    for j in range(n):
        if check[i][j] == 0:
            count = bfs(i, j, field[i][j])
            if field[i][j] == "W":
                w += count * count
            else:
                b += count * count

print(w, b)