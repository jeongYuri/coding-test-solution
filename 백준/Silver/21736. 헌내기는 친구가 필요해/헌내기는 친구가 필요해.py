import sys
from collections import deque

input_func = sys.stdin.readline

n, m = map(int, input_func().split())
board = []
cnt = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
school = [[0] * m for _ in range(n)]
q = deque()

for i in range(n):
    board.append(list(input_func().strip()))
    for j in range(len(board[i])):
        if board[i][j] == 'I':
            q.append([i, j])
            school[i][j] = 1

while q:
    for _ in range(len(q)):
        r, c = q.popleft()
        for i in range(4):
            nx, ny = r + dx[i], c + dy[i]
            if 0 <= nx < n and 0 <= ny < m and school[nx][ny] == 0 and board[nx][ny] != 'X':
                if board[nx][ny] == 'P':
                    cnt += 1
                school[nx][ny] = 1
                q.append([nx, ny])

if cnt:
    print(cnt)
else:
    print('TT')