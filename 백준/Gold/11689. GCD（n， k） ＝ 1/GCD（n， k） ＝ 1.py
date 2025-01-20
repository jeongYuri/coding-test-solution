import sys
import math
input = sys.stdin.readline
#오일러 피 함수 구현하기
n = int(input())
res = n
for p in range(2,int(math.sqrt(n))+1):
    if n%p==0:
        res -= res/p
        while n%p==0:
            n/=p
if n>1:
    res -= res/n
print(int(res))

