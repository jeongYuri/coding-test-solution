import sys
input = sys.stdin.readline
from itertools import combinations
l,c = map(int,input().split())
c = list(map(str,input().split()))
c.sort()
vowels = set('aeiou')
for combo in combinations(c,l):
    v_cnt = sum(1 for char in combo if char in vowels)
    c_cnt = l - v_cnt

    if v_cnt >= 1 and c_cnt >= 2:
        print(''.join(combo))


