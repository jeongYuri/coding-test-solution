import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
tmp = []
arr.sort()

if(n%2==1):
    tmp.append(arr[-1])
    arr = arr[:-1]
for i in range(len(arr)//2):
    tmp.append(arr[i]+arr[len(arr)-1-i])
print(max(tmp))