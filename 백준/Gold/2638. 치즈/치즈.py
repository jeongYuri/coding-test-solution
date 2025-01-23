import sys
from collections import deque
input = sys.stdin.readline

direction = [(-1,0),(1,0),(0,-1),(0,1)]
def fill_air(board, visited, start):
    q = deque([start])
    visited[start[0]][start[1]] = True
    while q:
        x, y = q.popleft()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:

                if board[nx][ny] >= 1:
                    board[nx][ny] += 1
                else:
                    visited[nx][ny] = True
                    q.append((nx, ny))

n,m = map(int,input().split())
board = [list(map(int, input().split())) for _ in range(n)]

time = 0
while True:
    visited = [[False]*m for _ in range(n)]
    fill_air(board, visited, (0,0))  

    melted = False
    for i in range(n):
        for j in range(m):
            if board[i][j] >= 3:
                board[i][j] = 0
                melted = True
            elif board[i][j] == 2:
                board[i][j] = 1

    if melted:
        time += 1
    else:
        break

print(time)
