from collections import deque
n,m,k = map(int,input().strip().split())
arr = [[0]*m for _ in range(n)]

for _ in range(k):
    r,c = map(int,input().split())
    arr[r-1][c-1]= 1

d = [(0,1),(0,-1),(1,0),(-1,0)]

def bfs(y,x):
    q = deque()
    q.append((y,x))
    arr[y][x] = 0
    cnt = 0
    while q:
        y,x = q.popleft()
        cnt +=1
        for dy, dx in d:
            ny,nx = y+dy, x+dx
            if (0<=ny<n) and(0<=nx<m) and arr[ny][nx]==1:
                arr[ny][nx] = 0
                q.append((ny,nx))
    return cnt

result = 1
for i in range(n):
    for j in range(m):
        if arr[i][j]==1:
            result = max(result,bfs(i,j))
print(result)