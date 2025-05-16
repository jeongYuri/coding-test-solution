N = int(input())
board = [[0] * 1001 for _ in range(1001)]

for n in range(1, N + 1):
    x, y, w, h = map(int, input().split())
    for i in range(y, y + h):
        board[i][x:x + w] = [n] * w  

for n in range(1, N + 1):
    cnt = 0
    for row in board:
        cnt += row.count(n)
    print(cnt)
