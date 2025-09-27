import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
miro = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(i,j):
    q = deque()
    q.append((i,j))
    visited[i][j] = True   
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if miro[nx][ny] != 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    miro[nx][ny] = miro[x][y] + 1
                    q.append((nx,ny))

bfs(0,0)
print(miro[n-1][m-1])
