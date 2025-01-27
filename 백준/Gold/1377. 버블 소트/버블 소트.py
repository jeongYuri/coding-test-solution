import sys
input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    arr.append((int(input()),i))
maxn = 0
arr = sorted(arr)
for i in range(n):
    if maxn<arr[i][1]-i:
        maxn = arr[i][1]-i
print(maxn+1)