def solution(numbers, target):
    ans = 0
    def dfs(idx,total):
        nonlocal ans
        if idx==len(numbers):
            if total==target:
                ans+=1
            return
        dfs(idx+1, total-numbers[idx])
        dfs(idx+1, total+numbers[idx])
    dfs(0,0)
    return ans