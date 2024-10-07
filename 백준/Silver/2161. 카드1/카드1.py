import sys
input = sys.stdin.readline
from collections import deque
n = int(input())
cards= deque(range(1, n + 1))
ans = []

while len(cards)>1:
    ans.append(cards.popleft())  # 첫 번째 카드를 버림
    cards.append(cards.popleft())
ans.append(cards.popleft())
print(*ans)