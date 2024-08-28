import sys
from collections import deque
input = sys.stdin.readline
def bfs(start_x, start_y):
    q = deque([(start_x, start_y)])
    distance[start_x][start_y] = 0  
    while q:
        x, y = q.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and distance[nx][ny] == -1 and land[nx][ny] == 1:
                distance[nx][ny] = distance[x][y] + 1
                q.append((nx, ny))

n, m = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(n)]
distance = [[-1] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if land[i][j] == 2:
            start_x, start_y = i, j
bfs(start_x, start_y)

for i in range(n):
    for j in range(m):
        if land[i][j] == 0:
            distance[i][j] = 0 
        elif land[i][j] == 1 and distance[i][j] == -1:
            distance[i][j] = -1  

for row in distance:
    print(*row)