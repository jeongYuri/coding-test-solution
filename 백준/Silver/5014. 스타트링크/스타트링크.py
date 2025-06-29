import sys
input = sys.stdin.readline
from collections import deque

def bfs(f,s,g,u,d):
    visited = [False]*(f+1) #총 층수가 f니까
    q = deque()
    q.append((s,0)) #현재층, 버튼 누른 횟수
    visited[s] = True

    while q:
        current, cnt = q.popleft()
        if current == g:
            return cnt
        next_up = current+u
        if next_up<=f and not visited[next_up]:
            visited[next_up] = True
            q.append((next_up,cnt+1))
        next_down = current-d
        if next_down>=1 and not visited[next_down]:
            visited[next_down] = True
            q.append((next_down,cnt+1))
    return "use the stairs"

f,s,g,u,d = map(int,input().split())
res = bfs(f,s,g,u,d)
print(res)