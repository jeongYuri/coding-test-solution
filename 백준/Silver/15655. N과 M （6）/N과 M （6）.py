import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
visited = [0] * (n)
temp = []
def solve(idx):
    global temp
    if len(temp)==m:
        print(*temp)
    for i in range(idx,n):
        if arr[i] not in temp:
            temp.append(arr[i])
            solve(i+1)
            temp.pop()
solve(0)
