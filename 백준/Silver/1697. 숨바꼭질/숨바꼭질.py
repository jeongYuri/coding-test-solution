import sys
from collections import deque
input = sys.stdin.readline
def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if v==m:
            return array[m]
        for next_v in (v-1,v+1,2*v):
            if 0 <= next_v < MAX and not array[next_v]:
                array[next_v] = array[v] + 1
                q.append(next_v)
MAX = 100001
n,m = map(int,input().split())
array = [0]*MAX
print(bfs(n))