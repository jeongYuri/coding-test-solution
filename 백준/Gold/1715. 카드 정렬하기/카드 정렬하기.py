import heapq
import sys
input = sys.stdin.readline

n = int(input())
cards = [int(input()) for _ in range(n)]
heapq.heapify(cards)
total = 0

while len(cards) > 1:
    sum_two = heapq.heappop(cards) + heapq.heappop(cards)
    total += sum_two
    heapq.heappush(cards, sum_two)
print(total)