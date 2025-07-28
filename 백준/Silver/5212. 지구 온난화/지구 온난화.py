import sys
input = sys.stdin.readline

r,c = map(int,input().split())

map = [list(input().strip()) for _ in range(r)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

sink =[]

for x in range(r):
    for y in range(c):
        if map[x][y]=='X':
            cnt = 0
            for d in range(4):
                nx,ny = x+dx[d],y+dy[d]
                if 0<= nx<r and 0<= ny<c:
                    if map[nx][ny]=='.':
                        cnt +=1
                else:
                    cnt +=1
            if cnt>=3:
                sink.append((x,y))

for x, y in sink:
    map[x][y]='.'
min_x, max_x = r,0
min_y,max_y = c,0

for x in range(r):
    for y in range(c):
        if map[x][y]=='X':
            min_x = min(min_x,x)
            max_x = max(max_x,x)
            min_y = min(min_y, y)
            max_y  = max(max_y,y)
for x in range(min_x, max_x+1):
    print(''.join(map[x][min_y:max_y + 1]))