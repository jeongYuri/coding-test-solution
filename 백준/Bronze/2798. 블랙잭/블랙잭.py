import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))
sums = [sum(combo) for combo in combinations(cards, 3)]
closest_sum = -1

for total in sums:
    if total <= m and total > closest_sum:
        closest_sum = total

print(closest_sum)