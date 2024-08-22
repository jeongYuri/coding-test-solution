import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int, input().split())
board = [list(input().strip()) for _ in range(r)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(sx, sy):
    q = deque()
    start_char = board[sx][sy]
    q.append((sx, sy, start_char))
    max_length = 0
    visited = set()  # (x, y, visited_chars_as_tuple)
    visited.add((sx, sy, start_char))

    while q:
        x, y, visited_chars = q.popleft()
        max_length = max(max_length, len(visited_chars))

        if max_length == 26:
            return 26

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                new_char = board[nx][ny]
                if new_char not in visited_chars:
                    new_visited_chars = visited_chars + new_char
                    if (nx, ny, new_visited_chars) not in visited:
                        visited.add((nx, ny, new_visited_chars))
                        q.append((nx, ny, new_visited_chars))

    return max_length


print(bfs(0, 0))