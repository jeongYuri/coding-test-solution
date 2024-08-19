def floyd(n, board):
    reach = [[board[i][j] for j in range(n)] for i in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if reach[i][k] and reach[k][j]:
                    reach[i][j] = 1
    return reach

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
res = floyd(n, board)

for row in res:
    print(' '.join(map(str, row)))
