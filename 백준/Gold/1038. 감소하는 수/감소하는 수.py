import sys
input = sys.stdin.readline
from itertools import combinations
n = int(input())
res = []

for i in range(1,11):
    for j in combinations(range(10),i):
        num = ''.join(list(map(str, reversed(list(j)))))
        res.append(int(num))
res.sort()
if n>= len(res):
    print(-1)
else:
    print(res[n])