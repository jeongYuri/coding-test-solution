import sys
input = sys.stdin.readline
n = int(input())
digit_cnt = len(str(n)) - 1
ans = 0
for i in range(digit_cnt):
    ans += 9 * (10 ** i) * (i + 1)
ans += (n - 10 ** digit_cnt + 1) * (digit_cnt + 1)

print(ans)