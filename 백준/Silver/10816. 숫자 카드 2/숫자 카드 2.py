import sys
from itertools import combinations

input = sys.stdin.readline
n = int(input())
card = [*map(int, input().split())]
m = int(input())
want = [*map(int, input().split())]
result = {}
for c in card:
    if c in result:
        result[c]+=1
    else:
        result[c]=1
for target in want:
    res = result.get(target)
    if res ==None:
        print(0,end=' ')
    else:
        print(res,end=' ')