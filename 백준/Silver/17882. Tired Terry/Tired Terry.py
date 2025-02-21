import sys

input = sys.stdin.readline

n, p, d = map(int, input().split())
sleep = input().strip()
current_sleep = 0
for i in range(p):
    if sleep[i] == 'Z':
        current_sleep += 1
cnt = 0
if current_sleep < d:
    cnt += 1
for i in range(1, n):
    if sleep[i - 1] == 'Z':
        current_sleep -= 1
    if sleep[(i + p - 1) % n] == 'Z':
        current_sleep += 1
    if current_sleep < d:
        cnt += 1

print(cnt)
