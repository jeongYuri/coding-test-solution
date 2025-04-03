import sys
from math import gcd
from itertools import combinations
input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    nums = list(map(int,input().split()))
    max_gcd = 0

    for a,b in combinations(nums,2):
        max_gcd = max(max_gcd, gcd(a,b))
    print(max_gcd)
