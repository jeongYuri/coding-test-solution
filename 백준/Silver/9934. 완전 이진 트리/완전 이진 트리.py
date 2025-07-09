import sys
input = sys.stdin.readline

def sol(start, end, level):
    if start==end:
        ans[level].append(tree[start])
        return
    mid = (start+end)//2
    ans[level].append(tree[mid])
    sol(start, mid-1,level+1)
    sol(mid+1, end, level+1)

level = int(input())
tree = list(map(int,input().split()))
l = len(tree)
ans = [[]for _ in range(level)]

sol(0,l-1,0)
for a in ans:
    print(*a)

