import sys
import math
input = sys.stdin.readline

n, l = map(int,input().split())

for i in range(l, 101):
    x = n-(i*(i+1)/2)
    ans = ""
    if(x%i)==0:
        x = int(x/i)
        if x>=-1:
            for j in range(1,i+1):
                ans +=f"{x+j} "
            print(ans)
            break
else:
    print(-1)
