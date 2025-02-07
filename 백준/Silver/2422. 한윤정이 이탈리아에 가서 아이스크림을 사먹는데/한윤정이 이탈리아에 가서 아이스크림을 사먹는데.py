import sys
from collections import defaultdict
from itertools import combinations
input = sys.stdin.readline


n,m = map(int,input().split()) #n은 아이스크림 종류 수, m은 섞으면 싫음...
hate = defaultdict(set)
for _ in range(m):
    a,b = map(int,input().split())
    hate[a].add(b)
    hate[b].add(a)
icecream = [i for i in range(1,n+1)]
combi = list(combinations(icecream,3))
valid_combi = []
for c in combi:
    a,b,c = sorted(c)
    if not(b in hate[a] or c in hate[a] or c in hate[b]):
        valid_combi.append((a,b,c))
print(len(valid_combi))
