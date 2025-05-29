import sys
from collections import deque
input = sys.stdin.readline

n = int(input()) #돌다리의 돌 개수
stone = list(map(int,input().split())) #돌
s = int(input())-1 #출발점

visited = [False] * n
q = deque()
q.append(s)
visited[s] = True
cnt = 1

while q:
    now = q.popleft()
    for move in [-stone[now],stone[now]]:
        next_pos = now + move
        if 0<= next_pos <n and not visited[next_pos]:
            visited[next_pos] = True
            q.append(next_pos)
            cnt +=1
print(cnt)