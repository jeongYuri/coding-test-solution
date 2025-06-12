from collections import deque
def solution(land):
    n,m = len(land), len(land[0])
    
    visited  = [[0] * m for _ in range(n)]
    col_list = [0] * m
    
    for i in range(n):
        for j in range(m):
            if land[i][j]==1 and not visited[i][j]:
                visited[i][j] = 1
                q = deque([(i,j)])
                oil = 0
                cols = set()
                
                while q:
                    x,y = q.popleft()
                    oil +=1
                    cols.add(y)
                    
                    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]: #상,하,좌,우
                        nx, ny = x+dx, y+dy
                        if 0<=nx<n and 0<=ny<m and land[nx][ny]==1 and not visited[nx][ny]:
                            visited[nx][ny] = 1
                            q.append((nx,ny))
                for col in cols:
                    col_list[col] += oil
    return max(col_list)
                            
