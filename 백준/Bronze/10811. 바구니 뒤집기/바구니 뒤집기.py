import sys
input = sys.stdin.readline


n,m = map(int,input().split())
baskets = [i for i in range(1,n+1)]
for i in range(m):
    i,j = map(int,input().split())
    baskets[i-1:j] = reversed(baskets[i-1:j])
print(*baskets)


