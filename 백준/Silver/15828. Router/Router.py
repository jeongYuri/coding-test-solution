import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
router = deque()

while True:
    info = int(input()) #발생한 시간순서대로 -> 그렇다면 먼저 들어온 친구들은 먼저 나가야함..
    if info == -1:
        break
    if info>0:
        if len(router)<n:
            router.append(info)
    elif info == 0:
        if router:
            router.popleft() #가장 먼저 들어온 패킷 제거

if router:
    print(*router)
else:
    print("empty")