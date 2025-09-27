import sys
input  = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
arr.sort()
m = int(input())
brr = list(map(int,input().split()))
res =[]

for i in range(m):
    find = False
    target = brr[i]
    start = 0
    end = len(arr)-1
    while start<=end:
        mid = int((start+end)/2)
        midv = arr[mid]
        if midv>target:
            end = mid-1
        elif midv<target:
            start = mid+1
        else:
            find =True
            break
    if find:
        print(1)
    else:
        print(0)