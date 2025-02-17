import sys
import math
from itertools import combinations
input = sys.stdin.readline

numbers = list(map(int,input().split()))
res = float('inf')
def lcm(a,b):
    return abs(a*b)//math.gcd(a,b)

for r in range(3,6): #적어도 세 개로 나누어 지는 가장 작은 자연수
    for comb in combinations(numbers, r):
        lcm_value = comb[0]
        for num in comb[1:]:
            lcm_value = lcm(lcm_value,num)
        res = min(res, lcm_value)
print(res)