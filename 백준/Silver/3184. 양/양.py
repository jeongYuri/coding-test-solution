import sys
from collections import deque
input = sys.stdin.readline
r,c = map(int,input().split())
madang = [list(input().rstrip()) for _ in range(r)] #글자 '.' (점)은 빈 필드를 의미하며, 글자 '#'는 울타리를, 'o'는 양, 'v'는 늑대를 의미
visited = [[False]*c for _ in range(r)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def bfs(x,y):
    q = deque([(x, y)])
    visited[y][x] = True
    sheep, wolf = 0,0
    if madang[y][x]=='o':
        sheep +=1
    elif madang[y][x] =='v':
        wolf+=1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < c and 0 <= ny < r and not visited[ny][nx] and madang[ny][nx] != '#':

                q.append((nx,ny))
                visited[ny][nx] = True
                if madang[ny][nx]=='o':
                    sheep+=1
                elif madang[ny][nx]=='v':
                    wolf+=1
    return sheep, wolf
def solve():
    total_s, total_w = 0,0
    for x in range(c):
        for y in range(r):
            if madang[y][x]!= '#' and not visited[y][x]:
                sheep,wolf = bfs(x,y)
                if sheep>wolf:
                    total_s += sheep
                else:
                    total_w += wolf

    print(total_s, total_w)
solve()
