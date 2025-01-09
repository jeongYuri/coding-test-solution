import sys
from collections import deque

input = sys.stdin.readline

def knight(l, start, target):
    directions = [
        (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)
    ]
    if start == target:
        return 0
    visited = [[False] * l for _ in range(l)]
    q = deque([(start[0], start[1], 0)]) 
    visited[start[0]][start[1]] = True

    while q:
        x, y, moves = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                if (nx, ny) == target:
                    return moves + 1
                q.append((nx, ny, moves + 1))
                visited[nx][ny] = True

    return -1

tc = int(input())
result = []
for _ in range(tc):
    l = int(input())
    start = tuple(map(int, input().split()))  # 시작 좌표
    target = tuple(map(int, input().split()))  # 목표 좌표
    result.append(knight(l, start, target))

for res in result:
    print(res)
