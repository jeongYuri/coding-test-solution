import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
board = [list(map(int, list(input().strip()))) for _ in range(n)]
visited = [[[0]*2 for _ in range(m)] for _ in range(n)] #0은 벽 안 부순 상태, 1은 부순상태

def bfs():
    q = deque()
    q.append((0,0,0))
    visited[0][0][0] = 1 #시작 위치 방문(거리 = 1)

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    while q:
        x,y, b = q.popleft()
        if x==n-1 and y== m-1:
            return visited[x][y][b]
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<= nx<n and 0<=ny<m:
                if board[nx][ny] == 0 and visited[nx][ny][b]==0:
                    visited[nx][ny][b] = visited[x][y][b]+1
                    q.append((nx,ny,b))
                elif board[nx][ny]==1 and b==0 and visited[nx][ny][1]==0:
                    visited[nx][ny][1] = visited[x][y][0]+1
                    q.append((nx,ny,1))
    return -1
print(bfs())