from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1:
                q.append((nx, ny))
                board[nx][ny] = board[x][y] + 1
    return board[n-1][m-1]
n, m = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
print(bfs(0,0))