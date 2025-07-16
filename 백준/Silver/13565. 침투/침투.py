import sys
input = sys.stdin.readline
from collections import deque
m,n = map(int,input().split())
board = [list(map(int, input().strip())) for _ in range(m)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [[False]*n for _ in range(m)]

q = deque()

for i in range(n):
    if board[0][i]==0:
        q.append((0,i))
        visited[0][i] = True

while q:
    x,y = q.popleft()

    if x==m-1: #맨 아래줄에 도달하면 성공
        print("YES")
        break

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0<= nx <m and 0<=ny<n:
            if not visited[nx][ny] and board[nx][ny]==0:
                visited[nx][ny] = True
                q.append((nx,ny))
else:
    print("NO")