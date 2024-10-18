import sys
n,m = map(int,input().split())
ans = []
def backtrack(depth):
    if len(ans)==m:
        print(' '.join(map(str,ans)))
        return
    for i in range(depth, n + 1): 
        ans.append(i)
        backtrack(i + 1)  
        ans.pop()


backtrack(1)
