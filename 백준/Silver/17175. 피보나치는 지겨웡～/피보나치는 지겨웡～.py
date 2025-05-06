import sys
input = sys.stdin.readline

MOD = 10**9 + 7
n = int(input())

cnt = [0] * (n + 2)

cnt[0] = 1
cnt[1] = 1

for i in range(2, n + 1):
    cnt[i] = (cnt[i - 1] + cnt[i - 2] + 1) % MOD

print(cnt[n])
