import sys

input = sys.stdin.readline
MAX_N = 1_000_000

isPrime = [True] * (MAX_N + 1)
isPrime[0] = isPrime[1] = False 
for i in range(2, int(MAX_N ** 0.5) + 1):
    if isPrime[i]:
        for j in range(i * i, MAX_N + 1, i):
            isPrime[j] = False

def gold(n):
    cnt = 0
    for p in range(2, n // 2 + 1):
        if isPrime[p] and isPrime[n - p]:
            cnt += 1
    return cnt

t = int(input().strip())
res = []
for _ in range(t):
    n = int(input().strip())
    res.append(str(gold(n)))

sys.stdout.write("\n".join(res) + "\n")
