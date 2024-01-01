import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input().rstrip())
matrix = [list(input().rstrip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

threec, twoc = 0,0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    visited[x][y]=True
    current_c = matrix[x][y]

    for k in range(4):
        nx = x+dx[k]
        ny = y+dy[k]
        if(0<=nx<n) and (0<=ny<n):
            if visited[nx][ny]==False:
                if matrix[nx][ny] ==current_c:
                    dfs(nx,ny)
for i in range(n):
    for j in range(n):
        if visited[i][j]==False:
            dfs(i,j)
            threec +=1
        if matrix[i][j]=='R':
            matrix[i][j]='G'
visited =[[False]* n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if visited[i][j]==False:
            dfs(i,j)
            twoc+=1
print(threec,twoc)