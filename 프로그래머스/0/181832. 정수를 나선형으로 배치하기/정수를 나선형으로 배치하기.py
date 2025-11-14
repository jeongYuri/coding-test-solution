def solution(n):
    board = [[0]*n for _ in range(n)]
    dx = [0, 1, 0, -1]   
    dy = [1, 0, -1, 0]

    x, y, d = 0, 0, 0    
    
    for num in range(1, n*n + 1):
        board[x][y] = num

        nx = x + dx[d]
        ny = y + dy[d]

    
        if nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny] != 0:
            d = (d + 1) % 4
            nx = x + dx[d]
            ny = y + dy[d]

        x, y = nx, ny

    return board
