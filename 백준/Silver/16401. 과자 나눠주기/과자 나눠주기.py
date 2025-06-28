import sys
input = sys.stdin.readline

def snack_length(m, snack):
    start, end = 1,max(snack)
    res = 0
    while start<=end:
        mid = (start+end)//2
        total = sum(s//mid for s in snack)
        if total>=m:
            res = mid
            start = mid+1
        else:
            end = mid-1
    return res
m,n =map(int,input().split())

snack = list(map(int,input().split()))

print(snack_length(m, snack))