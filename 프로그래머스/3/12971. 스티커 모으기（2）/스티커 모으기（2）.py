def max_sum(arr):
    dp = [0] * len(arr)
    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])
    for i in range(2, len(arr)):
        dp[i] = max(dp[i-1], dp[i-2] + arr[i])
    return dp[-1]

def solution(sticker):
    n = len(sticker)
    
    if n == 1:
        return sticker[0]
    if n == 2:
        return max(sticker)
    
    case1 = max_sum(sticker[:-1])
    case2 = max_sum(sticker[1:])
    
    return max(case1, case2)
