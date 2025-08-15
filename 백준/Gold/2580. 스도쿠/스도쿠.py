import sys
input = sys.stdin.readline

sudo = [list(map(int, input().split())) for _ in range(9)]
blanks = [(i, j) for i in range(9) for j in range(9) if sudo[i][j] == 0]

def is_possible(x, y, n):
    if n in sudo[x]: return False
    for i in range(9):
        if sudo[i][y] == n:
            return False
    nx = (x // 3) * 3
    ny = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if sudo[nx + i][ny + j] == n:
                return False
    return True

def dfs(idx):
    if idx == len(blanks):
        for row in sudo:
            print(*row)
        sys.exit(0)
    x, y = blanks[idx]
    for n in range(1, 10):
        if is_possible(x, y, n):
            sudo[x][y] = n
            dfs(idx + 1)
            sudo[x][y] = 0

dfs(0)
