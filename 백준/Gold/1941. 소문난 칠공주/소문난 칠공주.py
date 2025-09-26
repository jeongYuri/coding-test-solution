import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline
seat = []
for _ in range(5):
    seat.append(list(input().strip()))
direct = [(-1, 0), (1, 0), (0, -1), (0, 1)]
positions = [(i, j) for i in range(5) for j in range(5)]
comb = list(combinations(positions, 7))

ans = 0

def checkSom(combi):
    dasom = 0
    for x, y in combi:
        if seat[x][y] == 'S':
            dasom += 1
    return True if dasom >= 4 else False

def check(combi):
    visited = [False] * 7

    q = deque()
    q.append(combi[0])
    visited[0] = True
    count = 1

    while q:
        x, y = q.popleft()
        for d in direct:
            nx = x + d[0]
            ny = y + d[1]
            if (nx, ny) in combi:
                nextIdx = combi.index((nx, ny))

                if not visited[nextIdx]:
                    q.append((nx, ny))
                    visited[nextIdx] = True
                    count += 1

    return True if count == 7 else False


for combi in comb:
    if checkSom(combi):
        if check(combi):
            ans += 1

print(ans)