import sys
input = sys.stdin.readline

def dfs(idx):
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return
    former = 0
    for i in range(idx+1, n):
        if not isUsed[i] and nums[i] != former:
            arr.append(nums[i])
            isUsed[i] = 1
            former = nums[i]
            dfs(i)
            arr.pop()
            isUsed[i] = 0

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
arr = []
isUsed = [0] * n

dfs(-1)