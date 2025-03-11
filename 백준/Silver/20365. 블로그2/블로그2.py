import sys
input = sys.stdin.readline

n = int(input())
title = input().strip()

blue = 0
red = 0

if title[0]=='B':
    blue +=1
else:
    red +=1

for i in range(1,len(title)):
    if title[i]!=title[i-1]:
        if title[i]=='B':
            blue +=1
        else:
            red+=1
res = min(blue, red)+1
print(res)


