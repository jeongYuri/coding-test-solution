from collections import deque
def solution(maps):
    ans = 0
    q = deque()
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    q.append((0,0)) #0부터 시작이니까..
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            n = len(maps)
            m = len(maps[0])
            if(0<=nx<n and 0<=ny<m and maps[nx][ny]==1):
                maps[nx][ny] = maps[x][y]+1
                q.append((nx,ny))
    ans = maps[n-1][m-1]
    if ans ==1:
        return -1
    return ans