import sys
input = sys.stdin.readline

x, y = map(int,input().split())
z = (y*100)//x
if z>98:
    print(-1)
    exit()
s,e = 0,x
while s<e:
    mid = (s+e)//2
    if(y+mid)*100 // (x+mid) !=z:
        e = mid
    else:
        s = mid+1
mid = (s+e)//2
print(mid)