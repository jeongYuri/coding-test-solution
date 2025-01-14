n,m = map(int,input().split())
j = int(input())
apples = [int(input())for _ in range(j)]

left = 1
right = m
total = 0

for pos in apples:
    if left<=pos<=right:
        continue
    elif pos<left:
        total += left-pos
        left = pos
        right = left+m-1
    else:
        total += pos-right
        right = pos
        left = right-m+1
print(total)