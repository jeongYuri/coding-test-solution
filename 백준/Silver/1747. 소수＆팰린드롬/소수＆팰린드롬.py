import sys
import math
input = sys.stdin.readline
n = int(input())
a =[0]*(10000001)
for i in range(2,len(a)):
    a[i] = i

for i in range(2,int(math.sqrt(len(a)+1))):
    if a[i]==0:
        continue
    for j in range(i+i,len(a),i):
        a[j] = 0

def ispalindrome(target):
    temp = list(str(target))
    s = 0
    e = len(temp)-1
    while(s<e):
        if temp[s]!= temp[e]:
            return False
        s+=1
        e-=1
    return True
i = n
while True:
    if a[i]!=0:
        res = a[i]
        if(ispalindrome(res)):
            print(res)
            break
    i+=1