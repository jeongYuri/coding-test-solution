from collections import deque
t = int(input())
for tc in range(1,t+1):
    n = int(input())
    maps = [list(map(int,input()))for _ in range(n)]
    keys = [[99999] * n for _ in range(n)]
    keys[0][0] = 0  # 시작점은 0
    answer = 0
    q = deque()
    q.append((0,0))
    dx, dy = [-1,1,0,0],[0,0,-1,1]

    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < n:
                if keys[x][y] + maps[nx][ny] < keys[nx][ny]:
                    keys[nx][ny] = keys[x][y] + maps[nx][ny]
                    q.append((nx, ny))
    answer = keys[-1][-1]
    print(f'#{tc} {answer}')
