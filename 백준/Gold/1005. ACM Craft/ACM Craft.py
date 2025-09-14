import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    time = [0] + list(map(int, input().split()))  # 건물 짓는 시간
    building = [[] for _ in range(n+1)]
    indegree = [0] * (n+1)

    for _ in range(k):
        x, y = map(int, input().split())
        building[x].append(y)
        indegree[y] += 1

    w = int(input())

    dp = [0] * (n+1)
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            dp[i] = time[i]
            q.append(i)

    while q:
        now = q.popleft()
        for nxt in building[now]:
            indegree[nxt] -= 1
            dp[nxt] = max(dp[nxt], dp[now] + time[nxt])
            if indegree[nxt] == 0:
                q.append(nxt)

    print(dp[w])
