import sys
input = sys.stdin.readline

n, k = map(int,input().split())
coin = []
count = 0
for _ in range(n):
    coin.append(int(input()))
coin.sort(reverse = True)

while k>0:
    for i in coin:
        if i<=k:
            count +=k//i
            k%=i
print(count)