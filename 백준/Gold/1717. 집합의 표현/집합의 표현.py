import sys
input = sys.stdin.readline
def same(parent,x):
    if parent[x]!=x:
        parent[x] = same(parent,parent[x])
    return parent[x]
def union(parent, rank, a,b):
    root_a = same(parent, a)
    root_b = same(parent, b)
    if root_a != root_b :
        if rank[root_a]<rank[root_b]:
            parent[root_a] = root_b
        elif rank[root_a]>rank[root_b]:
            parent[root_b] = root_a
        else:
            parent[root_b] = root_a
            rank[root_a]+=1
n,m = map(int,input().split())
parent = [i for i in range(n+1)]
rank = [0] *(n+1)
res = []
for _ in range(m):
    op,a,b = map(int,input().split())
    if op==0: #합집합
        union(parent, rank,a,b)
    elif op==1: #같은지 확인
        if same(parent,a)==same(parent,b):
            res.append("YES")
        else:
            res.append("NO")
print("\n".join(res))