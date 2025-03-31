import sys
input = sys.stdin.readline

board = [list(map(int,input().split()))for _ in range(5)]
unique_number = set()

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y,num):
    if len(num)==6:
        unique_number.add(num)
        return
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0<= nx<5 and 0<=ny<5:
            dfs(nx,ny,num+str(board[nx][ny]))
for i in range(5):
    for j in range(5):
        dfs(i,j,str(board[i][j]))
print(len(unique_number))

