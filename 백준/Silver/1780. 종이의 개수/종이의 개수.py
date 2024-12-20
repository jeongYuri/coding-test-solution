import sys
input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
res = {-1: 0, 0: 0, 1: 0}

def divide(row, col, size):
    start = paper[row][col]
    if all(paper[i][j] == start for i in range(row, row + size) for j in range(col, col + size)):
        res[start] += 1
        return

    next_size = size // 3
    for i in range(3):
        for j in range(3):
            divide(row + i * next_size, col + j * next_size, next_size)

divide(0, 0, n)
print(res[-1])
print(res[0])
print(res[1])