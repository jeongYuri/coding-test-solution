import sys
input = sys.stdin.readline
N = int(input())
G = list(map(int,input().split()))
G.sort()
count = 0

for t in range(N):
  i = 0
  j = N-1
  find = G[t]
  while i<j:
    if G[i]+G[j]==find:
      if i!=t and j != t:
        count +=1
        break
      elif i==t:
        i+=1
      elif j==t:
        j-=1
    elif G[i]+G[j]>find:
        j-=1
    else:
        i+=1
      
print(count)
