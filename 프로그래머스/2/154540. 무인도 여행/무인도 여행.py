from collections import deque
def bfs(x,y,maps, visited,dx,dy):
    q = deque()
    q.append((x,y))
    visited[y][x] = True
    total = int(maps[y][x]) #시작점
    while q:
        cx,cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0<=nx<len(maps[0]) and 0<=ny<len(maps):
                if not visited[ny][nx] and maps[ny][nx] !='X':
                    visited[ny][nx] = True
                    total += int(maps[ny][nx])
                    q.append((nx,ny))
    return total
def solution(maps):
    answer = []
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    visited = [[False] * len(maps[0]) for _ in range(len(maps))] 
              
    for y in range(len(maps)):
        for x in range(len(maps[0])):
               if not visited[y][x] and maps[y][x] != "X":
                    answer.append(bfs(x, y, maps, visited, dx, dy))
    if not answer:
        return [-1]
    return sorted(answer)