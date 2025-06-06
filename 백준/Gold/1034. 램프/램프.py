import sys
input = sys.stdin.readline
from collections import Counter

n, m = map(int,input().split())
lamp = [input().strip() for _ in range(n)]
k = int(input())
counter = Counter(lamp)

max_on = 0

for pattern, cnt in counter.items():
    zero_cnt = pattern.count('0')

    if zero_cnt<=k and (k-zero_cnt)%2==0:
        max_on = max(max_on, cnt)
print(max_on)