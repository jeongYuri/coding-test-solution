import sys
input = sys.stdin.readline

def compress(y, x, size):
    start = board[y][x]
    for row in range(y, y + size):
        for col in range(x, x + size):
            if board[row][col] != start:
                half = size // 2
                top_left = compress(y, x, half)
                top_right = compress(y, x + half, half)
                bottom_left = compress(y + half, x, half)
                bottom_right = compress(y + half, x + half, half)
                return f"({top_left}{top_right}{bottom_left}{bottom_right})"
    return start

n = int(input())
board = [list(input().strip()) for _ in range(n)]
result = compress(0, 0, n)
print(result)
