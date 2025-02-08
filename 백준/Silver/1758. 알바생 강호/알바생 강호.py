import sys
input = sys.stdin.readline


n = int(input())
tip = [int(input())for _ in range(n)]
tip.sort(reverse=True)

ans = 0
for i in range(n):
    temp = tip[i]-i
    if temp>0:
        ans += temp
print(ans)