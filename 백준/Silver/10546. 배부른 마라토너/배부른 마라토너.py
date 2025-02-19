import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())

participants = [input().rstrip() for _ in range(n)]
finishers = [input().rstrip() for _ in range(n - 1)]
counter = Counter(participants)

for finisher in finishers:
    counter[finisher] -= 1
for name, count in counter.items():
    if count == 1:
        print(name)
        break
