import sys
input = sys.stdin.readline
n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr = sorted(arr)
print(arr[m-1])