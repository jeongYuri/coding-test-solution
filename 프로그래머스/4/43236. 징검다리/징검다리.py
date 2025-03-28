def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks.append(distance)
    start , end = 0,distance
    while start<=end:
        mid = (start+end)//2
        cnt = 0
        current = 0
        for rock in rocks:
            if rock - current < mid:
                cnt +=1 #삭제해야하는 바위수
            else:
                current = rock
        if cnt>n:
            end = mid-1
        else:
            answer = mid
            start = mid+1
                
    return answer