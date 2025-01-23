import heapq
import sys
input = sys.stdin.readline


def draw_star(n):
    if n == 1:
        return ['*']
    smaller = draw_star(n // 3)
    res = []
    for line in smaller:
        res.append(line * 3)
    for line in smaller:
        res.append(line + ' ' * (n // 3) + line)
    for line in smaller:
        res.append(line * 3)
    return res

n = int(input())
ans = draw_star(n)
print('\n'.join(ans))
