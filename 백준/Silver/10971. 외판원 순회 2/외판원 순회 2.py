import sys
input = sys.stdin.readline

n = int(input())
costs = [list(map(int,input().split()))for _ in range(n)]
visited = [0]*n #방문 여부
sum_c = 0 #방문 비용 합
ans = sys.maxsize

def dfs(depth, x):
    global sum_c, ans
    if depth == n-1: #종료 조건임
        if costs[x][0]:
            sum_c += costs[x][0]
            if sum_c < ans:
                ans = sum_c
            sum_c -= costs[x][0]
        return
    for i in range(1,n):
        if visited[i]== 0 and costs[x][i]: #방문 안한 도시일경우
            visited[i] = 1 #방문 체크
            sum_c += costs[x][i]#방문 비용 합치기
            dfs(depth+1,i)
            visited[i] = 0
            sum_c -= costs[x][i]#재귀 종료시 초기화
dfs(0,0)
print(ans)