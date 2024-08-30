import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(n)]
height_counts = {}
max_height = 0
min_height = 256

for i in range(n):
    for j in range(m):
        height = land[i][j]
        if height in height_counts:
            height_counts[height] += 1
        else:
            height_counts[height] = 1
        max_height = max(max_height, height)
        min_height = min(min_height, height)

ans = sys.maxsize
idx = 0

for floor in range(min_height, max_height + 1):
    exceed, lack = 0, 0
    for height in height_counts:
        if height > floor:
            exceed += (height - floor) * height_counts[height]
        elif height < floor:
            lack += (floor - height) * height_counts[height]

    if exceed + b >= lack:
        time = exceed * 2 + lack
        if time <= ans:
            ans = time
            idx = floor

print(ans, idx)
