import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
arr = sorted(list(map(int, input().split())))
temp = []
def solve():
    if len(temp)==m:
        print(*temp)
        return
    for i in range(n):
        temp.append(arr[i])
        solve()
        temp.pop()
solve()
