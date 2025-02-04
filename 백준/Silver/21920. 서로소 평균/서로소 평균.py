import sys
import math
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
x = int(input())

total = 0
cnt = 0

for a in arr:
    if math.gcd(a,x)==1:
        total +=a
        cnt +=1
average = total/cnt if cnt>0 else 0

print("{0:.6f}".format(average))
