import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(input().split())
    if n>32:
        print(0)
    else:
        ans = 100000
        m = []
        def dfs(start):
            global ans
            if len(m)==3:
                temp = 0
                for i in range(4):
                    if(m[0][i]!=m[1][i]):
                        temp +=1
                    if (m[1][i] != m[2][i]):
                        temp += 1
                    if (m[2][i] != m[0][i]):
                        temp += 1
                ans = min(ans,temp)
                return
            for i in range(start, n):
                m.append(arr[i])
                dfs(i+1)
                m.pop()
        dfs(0)
        print(ans)