import sys
input = sys.stdin.readline

n = int(input())
target = int(input())
snail = [[0]*n for _ in range(n)]

dr = [1,0,-1,0]
dc = [0,1,0,-1]

r,c = 0,0
direction = 0
num = n*n

snail[r][c] = num
num-=1

while num>0:
    nr = r+dr[direction]
    nc = c+dc[direction]
    if nr<0 or nr>=n or nc<0 or nc>=n or snail[nr][nc]!=0:
        direction = (direction+1)%4
        nr = r+dr[direction]
        nc = c+dc[direction]

    snail[nr][nc] = num
    num -=1
    r,c = nr,nc
pos_r, pos_c = 0,0
for i in range(n):
    for j in range(n):
        if snail[i][j]==target:
            pos_r,pos_c = i+1, j+1
for row in snail:
    print(*row)
print(pos_r,pos_c)
