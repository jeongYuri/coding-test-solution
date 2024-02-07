import sys
from collections import deque
input = sys.stdin.readline
v= int(input())
tree = [[]for _ in range(v+1)]
for _ in range(v):
    data = list(map(int,input().split()))
    cnt_n = data[0]
    idx = 1
    while data[idx]!=-1:
        adj_n,adj_c = data[idx],data[idx+1]
        tree[cnt_n].append((adj_n,adj_c))
        idx+=2

def bfs(start):
    q = deque()
    q.append((start,0))
    visited = [-1]*(v+1)
    visited[start]=0
    res = [0,0]
    while q:
        cnt_n,cnt_d = q.popleft()
        for adj_n,adj_d in tree[cnt_n]:
            if visited[adj_n]==-1:
                cal_d = cnt_d+adj_d
                q.append((adj_n,cal_d))
                visited[adj_n]=cal_d
                if res[1]<cal_d:
                    res[0] = adj_n
                    res[1]= cal_d
    return res
point,_ = bfs(1)

print(bfs(point)[1])