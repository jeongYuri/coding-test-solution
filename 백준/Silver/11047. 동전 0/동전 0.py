import sys
input = sys.stdin.readline

n,k = map(int,input().split())
cost = []
cnt = 0
for _ in range(n):
    cost.append(int(input()))
cost.reverse()
while k>0:
    for i in cost:
        if i<=k:
         cnt += k//i
         k%=i
print(cnt)