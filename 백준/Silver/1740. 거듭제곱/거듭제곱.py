import sys
input = sys.stdin.readline

k = bin(int(input()))[2:]
ans = 0

for i in range(len(k)):
    if int(k[i])==1:
        ans += 3**(len(k)-i-1)
print(ans)


