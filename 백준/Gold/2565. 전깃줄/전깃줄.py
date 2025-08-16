import sys
input = sys.stdin.readline

num = int(input())
lines = []
for _ in range(num):
    a,b = map(int,input().split())
    lines.append((a,b))
lines.sort() #a기준 오름차순 정렬
b_arr = [b for a,b in lines]
dp = [1]*num
for i in range(num):
    for j in range(i):
        if b_arr[j]<b_arr[i]:
            dp[i] = max(dp[i],dp[j]+1)
print(num-max(dp))