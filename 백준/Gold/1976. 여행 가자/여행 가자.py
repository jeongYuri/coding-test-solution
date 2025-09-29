import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
city = [list(map(int,input().split()))for _ in range(n)]
plan = list(map(int,input().split()))
parent =[0]*(n+1)

def find(a):
    if a== parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
    a = find(a)
    b = find(b)
    if a!=b:
        parent[b] = a

for i in range(1,n+1):
    parent[i] = i

for i in range(n):
    for j in range(n):
        if city[i][j] ==1:
            union(i+1,j+1)

idx = find(plan[0])
isConnect = True
for i in range(1,len(plan)):
    if idx != find(plan[i]):
        isConnect = False
        break

print('YES' if isConnect else 'NO')
