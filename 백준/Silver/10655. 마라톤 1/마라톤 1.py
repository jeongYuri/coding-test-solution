import sys
input = sys.stdin.readline

def distance(a, b):
    return abs(coord_list[a][0] - coord_list[b][0]) + abs(coord_list[a][1] - coord_list[b][1])

N = int(input())
coord_list = [list(map(int, input().split())) for _ in range(N)]

total_dist = 0
max_save = 0

for i in range(1, N):
    total_dist += distance(i - 1, i)

for i in range(1, N - 1):
    save = distance(i - 1, i) + distance(i, i + 1) - distance(i - 1, i + 1)
    max_save = max(max_save, save)

print(total_dist - max_save)