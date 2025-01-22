import heapq
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
if n==0:
    print(0)
    sys.exit()
books = list(map(int, input().split()))
temp = 0
res = 0
for i in range(n):
    if temp+books[i]>m:
        res +=1
        temp = books[i]
    else:
        temp += books[i]
if temp>0:
    res +=1
print(res)