import sys
input = sys.stdin.readline
from collections import deque
n = int(input())
game = []
for _ in range(n):
    row = list(map(int, input().split()))
    game.append(row)

direction = [(0, 1), (1, 0)] # 오른쪽 (0,1), 아래쪽 (1,0)

def bfs():
    q = deque([(0,0)]) #쩰리의 시작점
    visited = set([(0, 0)])

    while q:
        x,y = q.popleft()

        if game[x][y] == -1:
            print('HaruHaru')
            return

        step = game[x][y]
        for dx, dy in direction:
            nx, ny = x + dx * step, y + dy * step
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                visited.add((nx, ny))
                q.append((nx,ny))
    print('Hing')
bfs()