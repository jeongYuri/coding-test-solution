import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
G = list(map(int,input().split()))

G.sort()
count = 0
i = 0
j = N-1

while i<j:
  if G[i]+G[j]>M:
    j-=1
  elif G[i]+G[j]<M:
    i+=1
  else:
    count +=1
    i+=1
    j-=1
print(count)
