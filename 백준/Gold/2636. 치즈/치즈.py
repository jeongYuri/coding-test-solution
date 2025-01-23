import sys
from collections import deque
input = sys.stdin.readline
n,m  = map(int,input().split())
board = [list(map(int,input().split()))for _ in range(n)]

direction = [(-1,0),(1,0),(0,-1),(0,1)]

def bfs(a,b):
    visited = [[False]*m for _ in range(n)]
    q = deque()
    q.append((a,b))
    visited[a][b] = True
    while q:
        x,y = q.popleft()
        for dx, dy in direction:
            nx = x+dx
            ny = y+dy
            if 0<=nx<n and 0<=ny<m :
                if visited[nx][ny] == False:
                    if board[nx][ny]==1:
                        board[nx][ny] = 0
                        visited[nx][ny] = True
                        continue
                    if board[nx][ny] ==0:
                        visited[nx][ny] = True
                        q.append((nx,ny))
def check():
    cnt =0
    for i in range(n):
        for j in range(m):
            if board[i][j] ==1:
                cnt +=1
    return cnt
time = 0
last_cheese = 0
while True:
    cheese = check()
    if cheese>0:
        bfs(0,0)
        time+=1
        last_cheese = cheese
    elif cheese==0:
        break
print(time)
print(last_cheese)
