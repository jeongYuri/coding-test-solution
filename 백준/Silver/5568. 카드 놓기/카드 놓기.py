import sys
input = sys.stdin.readline
from itertools import permutations
n = int(input())
k = int(input())
cards = [input().strip() for _ in range(n)]
combs = set("".join(p) for p in permutations(cards, k))
print(len(combs))