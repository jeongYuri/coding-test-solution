import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())  # 소설을 구성하는 장의 수
    chapter = list(map(int, input().split()))

    s = [0] * (k + 1)
    for i in range(k):
        s[i + 1] = s[i] + chapter[i]

    dp = [[0] * k for _ in range(k)]
    opt = [[0] * k for _ in range(k)]
    for i in range(k):
        opt[i][i] = i  

    for size in range(1, k):  # 구간 크기
        for start in range(k - size):
            end = start + size
            dp[start][end] = float('inf')

            left = opt[start][end - 1]
            right = opt[start + 1][end]
            if left < start: 
                left = start
            if right > end - 1: 
                right = end - 1

            best_k = left
            for cut in range(left, right + 1):
                cost = dp[start][cut] + dp[cut + 1][end]
                if cost < dp[start][end]:
                    dp[start][end] = cost
                    best_k = cut

            dp[start][end] += s[end + 1] - s[start]
            opt[start][end] = best_k

    print(dp[0][k - 1])
