import sys

input = sys.stdin.readline

n, m = map(int, input().split())
res = []
visited = [False] * (n + 1)

def backtrack(depth):
    if depth == m:
        print(' '.join(map(str, res)))  
        return
    for i in range(1, n + 1):
        if not visited[i]:  
            visited[i] = True 
            res.append(i) 
            backtrack(depth + 1)  
            res.pop() 
            visited[i] = False  

backtrack(0)  
