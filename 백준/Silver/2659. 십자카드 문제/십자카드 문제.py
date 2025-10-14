import sys
input = sys.stdin.readline
from itertools import product

def get_clock_num(cards):
    nums = cards*2
    return min(int(''.join(map(str, nums[i:i+4])))for i in range(4))
cards = list(map(int,input().split()))
cnt = 0
n = len(cards)

target = get_clock_num(cards)

hubo = set()
for a,b,c,d in product(range(1,10),repeat = 4):
    hubo.add(get_clock_num([a,b,c,d]))
hubo = sorted(hubo)
print(hubo.index(target) + 1)