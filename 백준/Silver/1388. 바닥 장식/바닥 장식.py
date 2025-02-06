import sys
input = sys.stdin.readline

n, m = map(int, input().split())
room = [input().strip() for _ in range(n)]

cnt = 0

for i in range(n):
    prev = ''
    for j in range(m):
        if room[i][j] == '-' and room[i][j] != prev:
            cnt += 1
        prev = room[i][j]

for j in range(m):
    prev = ''
    for i in range(n):
        if room[i][j] == '|' and room[i][j] != prev:
            cnt += 1
        prev = room[i][j]

print(cnt)
