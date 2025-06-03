import sys
input = sys.stdin.readline

t = int(input())
while(t>0):

    a,b = map(int,input().split())
    t-=1
    res = pow(a, b, 10)
    if res==0:
        res = 10
    print(res)
