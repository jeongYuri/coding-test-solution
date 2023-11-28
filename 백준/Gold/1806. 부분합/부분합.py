import sys
input = sys.stdin.readline

n,s = map(int,input().split())
arr = [int(x) for x in sys.stdin.readline().rstrip().split()]
left = 0
right = 0
length = 100000
arr_sum = arr[0]

while left<=right:
    if arr_sum>=s:
        length = min(length,right-left+1)
        arr_sum -=arr[left]
        left+=1
    else:
        right +=1
        if right<n:
            arr_sum +=arr[right]
        else:
            break

if length == 100000:
    print(0)
else:
    print(length)
