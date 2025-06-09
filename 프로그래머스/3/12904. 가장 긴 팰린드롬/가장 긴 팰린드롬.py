def solution(s):
    max_len  = 1
    n = len(s)
    for start in range(n):
        for end in range(start+1, n+1):
            sub = s[start:end]
            if sub==sub[::-1]:
                max_len = max(max_len, end-start)
         
    return max_len