from collections import deque

def solution(board):
    rows, cols = len(board), len(board[0])
    start, goal = None, None
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 'R':
                start = (i, j)
            elif board[i][j] == 'G':
                goal = (i, j)

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visit = [[float('inf')] * cols for _ in range(rows)]
    visit[start[0]][start[1]] = 0
    queue = deque([start])
    
    while queue:
        x, y = queue.popleft()
        if (x, y) == goal:
            return visit[x][y]
        
        for dx, dy in directions:
            nx, ny = x, y
            while 0 <= nx + dx < rows and 0 <= ny + dy < cols and board[nx + dx][ny + dy] != 'D':
                nx += dx
                ny += dy
            
         
            if visit[nx][ny] > visit[x][y] + 1:
                visit[nx][ny] = visit[x][y] + 1
                queue.append((nx, ny))

    return -1
