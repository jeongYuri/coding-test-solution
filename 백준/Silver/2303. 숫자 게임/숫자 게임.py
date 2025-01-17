import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())
cards = [list(map(int, input().split())) for _ in range(n)]
max_score = 0
winner = 0
for i in range(n):
    hubo = list(combinations(cards[i], 3))
    score = max(sum(t) % 10 for t in hubo)
    if score >= max_score:
        max_score = score
        winner = i + 1

print(winner)
