import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())

road = [[] for _ in range(n+1)]
reverse = [[]for _ in range(n+1)]
indegree = [0]*(n+1)

for i in range(m):
    s,e,v = map(int,input().split())
    road[s].append((e,v))
    reverse[e].append((s,v))
    indegree[e]+=1

start, end = map(int,input().split())
q = deque()
q.append(start)
res = [0]*(n+1)

while q:
    now = q.popleft()
    for next in road[now]:
        indegree[next[0]] -=1
        res[next[0]] = max(res[next[0]],res[now]+next[1])
        if indegree[next[0]]==0:
            q.append(next[0])
cnt = 0
visited = [False]*(n+1)
q.clear()
q.append(end)
visited[end] = True

while q:
    now = q.popleft()
    for next in reverse[now]:
        if res[next[0]] + next[1]==res[now]:
            cnt+=1
            if not visited[next[0]]:
                visited[next[0]] = True
                q.append(next[0])
print(res[end])
print(cnt)