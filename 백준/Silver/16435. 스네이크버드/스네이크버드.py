import sys
input = sys.stdin.readline
n,l = map(int,input().split())
high = list(map(int,input().split()))
high.sort()
for h in high:
    if h<=l:
        l+=1
    else:
        break
print(l)
