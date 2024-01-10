def solution(n, times):
    answer = 0
    start, end = 0, max(times)*n
    while start<=end:
        mid = (start+end)//2
        cnt = 0
        for time in times:
            cnt += mid//time
        if cnt>=n:
            answer = mid
            end = mid-1
        else:
            start = mid+1
            
                
    return answer