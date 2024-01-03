from collections import deque
import sys
input = sys.stdin.readline
m, n, h = map(int, input().split())
board = [[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]
visit = [[[False] * m for _ in range(n)] for _ in range(h)]
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
q = deque()
res = 0

def bfs():
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx<0 or nx>=h or ny<0 or ny>=n or nz<0 or nz>= m:
                continue
            if board[nx][ny][nz] == 0 and not visit[nx][ny][nz]:
                q.append((nx, ny, nz))
                board[nx][ny][nz] = board[x][y][z] + 1
                visit[nx][ny][nz] = True

for i in range(h):
    for j in range(n):
        for k in range(m):
            if board[i][j][k] == 1 and not visit[i][j][k]:
                q.append((i, j, k))
                visit[i][j][k] = True

bfs()

for i in board:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
            res = max(res, max(j))

print(res - 1)
