from collections import deque
n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
vistd = [0]*(m+1)
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs(board,x,y):
    q = deque()
    board[x][y]=0
    q.append((x,y))
    count = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and board[nx][ny]==1:
                board[nx][ny]=0
                q.append([nx,ny])
                count +=1
    return count
paint = []
for i in range(n):
    for j in range(m):
        if board[i][j]==1:
            paint.append(bfs(board,i,j))
if len(paint)==0:
    print(len(paint))
    print(0)
else:
    print(len(paint))
    print(max(paint))
