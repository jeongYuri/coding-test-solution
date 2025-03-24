import sys
input = sys.stdin.readline
from collections import deque
n,m,k,x = map(int,input().split()) #도시의 개수, 도로의 개수, 거리 정보, 출발 도시의 번호
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b) #a번 도시에서 b번 도시로 이동하는 단방향..도로

distance = [-1]*(n+1)
distance[x] = 0 # 출발 도시의 거리는 0

q = deque([x])

while q:
    now = q.popleft()
    for next_city in graph[now]:
        if distance[next_city]==-1:
            distance[next_city] = distance[now]+1
            q.append(next_city)
res = [i for i in range(1,n+1) if distance[i]==k]
if res:
    for city in sorted(res):
        print(city)
else:
    print(-1)