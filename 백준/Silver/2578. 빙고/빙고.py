import sys
import math
input = sys.stdin.readline

bingo = [list(map(int,input().split()))for _ in range(5)]
talk = [list(map(int,input().split()))for _ in range(5)]

def check_bingo(board):
    cnt = 0
    for row in board:
        if sum(row)==0:
            cnt +=1
    for col in range(5):
        if sum(board[row][col] for row in range(5))==0:
            cnt+=1
    if sum(board[i][i] for i in range(5))==0:
        cnt +=1
    if sum(board[i][4-i] for i in range(5))==0:
        cnt +=1
    return cnt
cnt = 0
match = []
for i in range(5):
    for j in range(5):
        num = talk[i][j]
        cnt +=1
        for x in range(5):
            for y in range(5):
                if bingo[x][y] == num:
                    bingo[x][y] = 0

        if check_bingo(bingo)>=3:
            print(cnt)
            exit()