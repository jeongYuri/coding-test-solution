from bisect import bisect_left

def lis(seq):
    lis_seq = []  
    dp = [0] * len(seq)  

    for i, num in enumerate(seq):
        pos = bisect_left(lis_seq, num) 
        if pos == len(lis_seq):
            lis_seq.append(num) 
        else:
            lis_seq[pos] = num 
        dp[i] = pos + 1  
    
    return dp

n = int(input())
A = list(map(int, input().split()))

inc_dp = lis(A)

dec_dp = lis(A[::-1])[::-1]

result = []
for i in range(n):
    result.append(inc_dp[i] + dec_dp[i] - 1)

print(max(result))