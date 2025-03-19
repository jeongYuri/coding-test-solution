import sys
input = sys.stdin.readline

c,r = map(int,input().split())
k = int(input())

if k>r*c:
    print(0)
    sys.exit(0)
x,y,dir = 0,0,0
visited = [[False] * r for _ in range(c)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for _ in range(k - 1):
    visited[x][y] = True
    nx,ny = x+dx[dir],y+dy[dir]

    if nx<0 or ny<0 or nx>=c or ny>=r or visited[nx][ny]:
        dir = (dir+1)%4
        nx,ny = x+dx[dir],y+dy[dir]
    x,y = nx,ny
print(x + 1, y + 1)
