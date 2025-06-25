import sys
input = sys.stdin.readline

k,n,m = map(int,input().split())
res = k*n
if res<m:
    print(0)
else:
    print(res-m)
