def solution(board):
    if not board:
        return 0    
    n = len(board)
    m = len(board[0])
    dp = [0] * (m)
    ans = 0
    
    for i in range(n):
        prev = 0  
        for j in range(m):
            temp = dp[j]  
            if board[i][j] == 1:
                if i == 0 or j == 0:
                    dp[j] = 1  
                else:
                    dp[j] = min(dp[j], dp[j-1], prev) + 1
                ans = max(ans, dp[j]) 
            else:
                dp[j] = 0  
            prev = temp      
    return ans * ans  
