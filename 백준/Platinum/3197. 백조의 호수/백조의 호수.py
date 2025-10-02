import sys
input = sys.stdin.readline
from collections import deque

r, c = map(int, input().split())
lake = [list(input().strip()) for _ in range(r)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

visited = [[False] * c for _ in range(r)]
water_visited = [[False] * c for _ in range(r)]

swan_q = deque()
water_q = deque()
pos = []

for row in range(r):
    for col in range(c):
        if lake[row][col] in ('L', '.'):
            water_q.append((row, col))
            water_visited[row][col] = True
            if lake[row][col] == 'L':
                pos.append((row, col))

swan_q.append(pos[0])
visited[pos[0][0]][pos[0][1]] = True

day = 0
while True:
    
    next_swan = deque()
    found = False
    
    while swan_q and not found:
        x, y = swan_q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                visited[nx][ny] = True
                
                if lake[nx][ny] == 'X':
                    next_swan.append((nx, ny))
                else:
                    swan_q.append((nx, ny))
                    if nx == pos[1][0] and ny == pos[1][1]:
                        found = True
                        break
    
    if found:
        print(day)
        break
    
    swan_q = next_swan
    
    
    next_water = deque()
    while water_q:
        x, y = water_q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and not water_visited[nx][ny]:
                water_visited[nx][ny] = True
                
                if lake[nx][ny] == 'X':
                    lake[nx][ny] = '.'
                    next_water.append((nx, ny))
    
    water_q = next_water
    day += 1