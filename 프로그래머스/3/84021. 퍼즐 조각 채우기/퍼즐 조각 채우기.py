def extract_shapes(board, value):
    n = len(board)
    visited = [[False] * n for _ in range(n)]
    shapes = []

    def dfs(x, y, shape):
        if x < 0 or x >= n or y < 0 or y >= n:
            return
        if visited[x][y] or board[x][y] != value:
            return
        visited[x][y] = True
        shape.append((x, y))
        dfs(x + 1, y, shape)
        dfs(x - 1, y, shape)
        dfs(x, y + 1, shape)
        dfs(x, y - 1, shape)

    for i in range(n):
        for j in range(n):
            if not visited[i][j] and board[i][j] == value:
                shape = []
                dfs(i, j, shape)
                if shape:  
                    shapes.append(shape)

    return [normalize(shape) for shape in shapes]

def rotate_shape(shape):
    return normalize([(y, -x) for x, y in shape])

def normalize(shape):
    min_x = min(x for x, y in shape)
    min_y = min(y for x, y in shape)
    return sorted((x - min_x, y - min_y) for x, y in shape)

def can_fit(board_shape, table_shape):
    board_shape = normalize(board_shape)
    for _ in range(4):  
        if board_shape == normalize(table_shape):
            return True
        table_shape = rotate_shape(table_shape)
    return False

def fill_board(board_shapes, table_shapes):
    filled_count = 0
    used_shapes = [False] * len(table_shapes)  
    
    for board_shape in board_shapes:
        for i, table_shape in enumerate(table_shapes):
            if not used_shapes[i] and can_fit(board_shape, table_shape):
                filled_count += len(table_shape)
                used_shapes[i] = True  
                break
    
    return filled_count

def solution(game_board, table):
    board_shapes = extract_shapes(game_board, 0)
    table_shapes = extract_shapes(table, 1)
    return fill_board(board_shapes, table_shapes)
