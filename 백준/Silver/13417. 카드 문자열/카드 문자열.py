from collections import deque

for _ in range(int(input())):
    n = int(input())
    card = input().split()
    q = deque()
    q.append(card[0])
    stand = card[0]

    for i in range(1, len(card)):
        if stand >= card[i]:
            q.appendleft(card[i])
            stand = card[i]
        else:
            q.append(card[i])

    print(''.join(q))
