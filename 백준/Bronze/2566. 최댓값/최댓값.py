import sys
input = sys.stdin.readline

board = [list(map(int, input().rstrip().split())) for _ in range(9)]


max_num = -1
max_row, max_col = 0,0
for r in range(9):
    for c in range(9):
        if board[r][c]>=max_num:
            max_num = board[r][c]
            max_row = r+1
            max_col = c+1
print(max_num)
print(max_row, max_col)

