import sys
input = sys.stdin.readline

n,s = map(int,input().split())
arr = list(map(int,input().split()))
cnt = 0
ans = []
def solve(v):
    global cnt
    if sum(ans)==s and len(ans)>0:
        cnt +=1
    for i in range(v,n):
        ans.append(arr[i])
        solve(i+1)
        ans.pop()
solve(0)
print(cnt)
