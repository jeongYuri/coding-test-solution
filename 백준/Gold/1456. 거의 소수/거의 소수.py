import sys
import math
input = sys.stdin.readline

n,m = map(int,input().split())
a = [0]*10000001

for i in range(2,len(a)):
    a[i] = i
for i in range(2, int(math.sqrt(len(a)))+1):
    if a[i]==0:
        continue
    for j in range(i+i,len(a),i):
        a[j] = 0
cnt = 0
for i in range(2,10000001):
    if a[i]!=0:
        temp = a[i]
        while a[i]<= m/temp:
            if a[i]>=n/temp:
                cnt+=1
            temp = temp*a[i]
print(cnt)