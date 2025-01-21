import sys
sys = sys.stdin.readline
import math

Min,Max = map(int,input().split())
check = [False]*(Max-Min+1)
for i in range(2,int(math.sqrt(Max))+1):
    pow = i*i #제곱수
    start = int(Min/pow)
    if Min%pow!=0:
        start +=1
    for j in range(start, int(Max/pow)+1):
        check[int((j*pow)-Min)] = True
cnt = 0
for i in range(0,Max-Min+1):
    if not check[i]:
        cnt +=1
print(cnt)