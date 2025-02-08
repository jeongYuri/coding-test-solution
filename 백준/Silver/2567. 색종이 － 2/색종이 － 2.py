import sys
input = sys.stdin.readline

tc = int(input())
board = [[0]*102 for _ in range(102)] #도화지 크기를 여유롭게

#색종이 영역 표시
for _ in range(tc):
    x,y = map(int,input().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
            board[i][j] = 1

directions = [(0,1),(0,-1),(1,0),(-1,0)]
res = 0
for i in range(102):
    for j in range(102):
        if board[i][j]==1: #색종이부분만 탐색
            for dx, dy in directions:
                ni,nj = i+dx, j+dy
                if board[ni][nj]==0:
                    res +=1
print(res)
