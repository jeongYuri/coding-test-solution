from collections import deque
N,L = map(int,input().split())
md = deque()
now = list(map(int, input().split()))

for i in range(N):
  while md and md[-1][0]>now[i]:
    md.pop()
  md.append((now[i],i))
  if md[0][1]<=i-L:
    md.popleft()
  print(md[0][0],end=' ')