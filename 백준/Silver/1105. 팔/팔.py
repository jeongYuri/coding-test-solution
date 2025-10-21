import sys
input = sys.stdin.readline

l,r= input().split()

if len(l)!=len(r):
    print(0)
else:
    cnt = 0
    for x,y in zip(l,r):
        if x==y:
            if x=='8':
                cnt+=1
        else:
            break
    print(cnt)