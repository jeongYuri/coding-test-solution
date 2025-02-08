import sys
input = sys.stdin.readline

n,k = map(int,input().split())
res = k*(k+1)//2

if n<res:
    print(-1)
else:
    r = n - res
    if r%k==0:
        print(k-1)
    else:
        print(k)