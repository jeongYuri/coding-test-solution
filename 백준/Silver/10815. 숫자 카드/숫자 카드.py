import sys
input = sys.stdin.readline
n = int(input())
cards = list(map(int, input().split())) #상근 카드
m = int(input())
cards2 = list(map(int, input().split())) #상근..확인차..
res = []
card_set = set(cards)
for card in cards2:
    if card in card_set:
        res.append(1)
    else:
        res.append(0)
print(*res)

