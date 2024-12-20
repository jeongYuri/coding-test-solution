import sys
input = sys.stdin.readline
from itertools import combinations
while True :
    lotto = list(map(int,input().split()))
    if lotto[0]==0:
        break
    k = lotto[0]
    s = lotto[1:]
    for comb in combinations(s,6):
        print(' '.join(map(str,comb)))
    print()
