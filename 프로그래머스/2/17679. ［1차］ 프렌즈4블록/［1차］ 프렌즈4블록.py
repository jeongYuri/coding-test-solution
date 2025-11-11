def check(m, n, board):
    filter = [[0] * n for _ in range(m)]
    cnt = 0

    for i in range(m - 1):
        for j in range(n - 1):
            a, b, c, d = board[i][j], board[i][j+1], board[i+1][j], board[i+1][j+1]
            if a == b == c == d and a != '0':
                filter[i][j] = filter[i][j+1] = filter[i+1][j] = filter[i+1][j+1] = 1

    for i in range(m):
        for j in range(n):
            if filter[i][j] == 1:
                board[i][j] = '0'
                cnt += 1

    if cnt == 0:
        return 0  

    for j in range(n):
        stack = []
        for i in range(m-1, -1, -1): 
            if board[i][j] != '0':
                stack.append(board[i][j])
        for i in range(m-1, -1, -1):
            board[i][j] = stack.pop(0) if stack else '0'

    return cnt


def solution(m, n, board):
    board = [list(row) for row in board]
    answer = 0

    while True:
        removed = check(m, n, board)
        if removed == 0:
            break
        answer += removed

    return answer
