from collections import deque

n= int(input())
a = [[]for _ in range(n+1)]
for _ in range(n):
    data = list(map(int,input().split()))
    index = 0
    s = data[index]
    index +=1
    while True:
        e = data[index]
        if e==-1:
            break
        v = data[index+1]
        a[s].append((e,v))
        index +=2
distance = [0]*(n+1)
visited = [False]*(n+1)

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = True
    while q:
        now = q.popleft()
        for i in a[now]:
            if not visited[i[0]]:
                visited[i[0]]=True
                q.append(i[0])
                distance[i[0]] = distance[now] + i[1]
bfs(1)
Max =1
for i in range(2,n+1):
    if distance[Max]<distance[i]:
        Max = i
distance = [0]*(n+1)
visited = [False]*(n+1)
bfs(Max)
distance.sort()
print(distance[n])
