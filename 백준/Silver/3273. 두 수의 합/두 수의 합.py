import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
x = int(input())
cnt = 0
freq = {}

for ar in arr:
    comp = x-ar
    if comp in freq:
        cnt += freq[comp]
    freq[ar] = freq.get(ar,0)+1
print(cnt)



