def solution(n, times):
    answer = 0
    start, end = 0, max(times)*n #가장 느린 심사관이 모든 사람 처리하는 경우 생각
    while start<=end:
        cnt = 0
        mid = (start+end)//2
        for time in times:
            cnt += mid//time
        if cnt>=n:
            answer = mid
            end = mid-1
        else:
            start = mid+1
    return answer