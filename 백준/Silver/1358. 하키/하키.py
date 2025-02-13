import sys
input = sys.stdin.readline

w, h, x, y, p = map(int, input().split())
cnt = 0

for _ in range(p):
    a, b = map(int, input().split())

    # 직사각형 내부
    if (x <= a <= x + w) and (y <= b <= y + h):
        cnt += 1
        continue

    r = h / 2  # 반지름
    d1 = ((a - x) ** 2 + (b - (y + r)) ** 2) ** 0.5
    d2 = ((a - (x + w)) ** 2 + (b - (y + r)) ** 2) ** 0.5

    # 반원 내부
    if d1 <= r or d2 <= r:
        cnt += 1

print(cnt)
