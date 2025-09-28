import sys
from collections import deque
input =sys.stdin.readline

now = list(map(int,input().split()))

sender = [0,0,1,1,2,2]
receiver =[1,2,0,2,0,1]

visited = [[False for j in range(201)]for i in range(201)]
ans = [False]*201

def bfs():
    q = deque()
    q.append((0,0))
    visited[0][0] = True
    ans[now[2]] = True
    while q:
        now_node = q.popleft()
        a = now_node[0]
        b = now_node[1]
        c = now[2]-a-b
        for k in range(6):
            next = [a,b,c]
            next[receiver[k]] += next[sender[k]]
            next[sender[k]] = 0
            if next[receiver[k]]>now[receiver[k]]:
                next[sender[k]] = next[receiver[k]] - now[receiver[k]]
                next[receiver[k]] = now[receiver[k]]
            if not visited[next[0]][next[1]]:
                visited[next[0]][next[1]] = True
                q.append((next[0],next[1]))
                if next[0] == 0:
                    ans[next[2]] = True
bfs()
for i in range(len(ans)):
    if ans[i]:
        print(i,end=' ')