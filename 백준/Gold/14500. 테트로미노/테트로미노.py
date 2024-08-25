import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
max_score = -1

def dfs(depth, x, y, total):
    global max_score
    if depth == 4:
        max_score = max(max_score, total)
    elif (total + max_value * (4 - depth)) <= max_score:  # 가지치기
        return
    else:
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                visited[nx][ny] = True
                if depth == 2:  # ㅗ 모양을 처리하기 위한 조건
                    dfs(depth + 1, x, y, total + grid[nx][ny])
                dfs(depth + 1, nx, ny, total + grid[nx][ny])
                visited[nx][ny] = False


N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
max_value = max(map(max, grid)) 
for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(1, i, j, grid[i][j])
        visited[i][j] = False

print(max_score)
