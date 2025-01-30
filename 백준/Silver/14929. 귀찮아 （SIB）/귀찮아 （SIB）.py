import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
prefix_sum = [0] * (n + 1)
for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i-1] + arr[i-1]

result = 0
for i in range(n):
    result += arr[i] * (prefix_sum[n] - prefix_sum[i+1])

print(result)