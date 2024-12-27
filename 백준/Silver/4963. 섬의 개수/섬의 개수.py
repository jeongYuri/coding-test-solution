import sys
from collections import deque
input = sys.stdin.readline
def bfs(x,y,island,visited, w,h):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    q = deque([(x,y)])
    visited[y][x] = True
    while q:
        cx,cy = q.popleft()
        for dx,dy in directions:
            nx, ny = cx+dx, cy+dy
            if 0<=nx <w and 0<=ny<h and not visited[ny][nx] and island[ny][nx] ==1:
                visited[ny][nx] = True
                q.append((nx,ny))

while True:
    w, h = map(int,input().split())
    island = []
    if w==0 and h==0:
        break
    for _ in range(h):
        island.append(list(map(int,input().split())))
    cnt = 0
    visited = [[False for _ in range(w)]for _ in range(h)]

    #섬 탐색
    for y in range(h):
        for x in range(w):
            if island[y][x] ==1 and not visited[y][x]:
                bfs(x,y,island,visited, w,h)
                cnt +=1

    print(cnt)