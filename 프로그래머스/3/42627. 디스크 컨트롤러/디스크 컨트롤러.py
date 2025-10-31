import heapq
def solution(jobs):
    jobs.sort()
    h = []
    time,total_time,i = 0,0,0
    n = len(jobs)
    
    while i<n or h:
        while i<n and jobs[i][0]<=time:
            r,d = jobs[i]
            heapq.heappush(h,(d,r))
            i+=1
        if h:
            d,r = heapq.heappop(h)
            time+=d
            total_time+= time-r
        else:
            time = jobs[i][0]
        
    return total_time//n