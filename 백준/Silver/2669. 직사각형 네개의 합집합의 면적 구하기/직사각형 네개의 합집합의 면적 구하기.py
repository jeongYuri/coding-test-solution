import sys
input = sys.stdin.readline

grid = [[0] * 1001 for _ in range(1001)]
rectangles = [tuple(map(int, input().split())) for _ in range(4)]

for x1, y1, x2, y2 in rectangles:
    for x in range(x1, x2):
        for y in range(y1, y2):
            grid[x][y] = 1

total_area = sum(sum(row) for row in grid)
print(total_area)