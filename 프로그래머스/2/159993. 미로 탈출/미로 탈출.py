from collections import deque
def bfs(maps, start, target):
    rows, cols = len(maps), len(maps[0])
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    visited = [[False]*cols for _ in range(rows)]
    q = deque([(start[0],start[1],0)])
    visited[start[0]][start[1]] = True
    
    while q:
        x,y, dist = q.popleft()
        if maps[x][y]==target:
            return dist
        for dx, dy in directions : 
            nx,ny = x+dx, y+dy
            if 0<=nx<rows and 0<=ny<cols and not visited[nx][ny] and maps[nx][ny] !='X':
                visited[nx][ny] = True
                q.append((nx,ny,dist+1))
    return -1
def solution(maps):
    rows, cols = len(maps), len(maps[0])
    start = lever = exit = None #시작, 레버, 출구 위치 찾기
    for i in range(rows):
        for j in range(cols):
            if maps[i][j] =='S':
                start = (i,j)
            elif maps[i][j]=='L':
                lever= (i,j)
            elif maps[i][j] =='E':
                exit = (i,j)
    to_lever = bfs(maps, start,'L')
    if to_lever ==-1:
        return -1
    to_exit = bfs(maps, lever,'E')
    if to_exit ==-1:
        return -1
    return to_lever+to_exit