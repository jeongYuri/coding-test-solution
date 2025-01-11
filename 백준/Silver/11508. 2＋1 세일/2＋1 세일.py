import sys
input = sys.stdin.readline
n = int(input())
prices = [int(input()) for _ in range(n)]
prices.sort(reverse=True)

ans = 0
for i in range(n):
    if i%3==2:
        continue
    ans+= prices[i]
print(ans)