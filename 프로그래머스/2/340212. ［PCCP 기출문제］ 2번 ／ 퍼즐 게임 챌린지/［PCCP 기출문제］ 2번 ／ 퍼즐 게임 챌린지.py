def solution(diffs, times, limit):
    def get_time(level):
        total_time = 0
        for i in range(len(diffs)):
            diff = diffs[i]
            time_cur = times[i]
            time_prev = 0 if i == 0 else times[i - 1]
            
            if level >= diff:
                total_time += time_cur
            else:
                fail = diff - level
                total_time += fail * (time_cur + time_prev) + time_cur
                
            if total_time > limit:
                return float('inf')  
        return total_time
    
    level = 1
    jump = 100000  
    while jump > 0:
        while get_time(level) > limit:
            level += jump
        level = max(1, level - jump)  
        jump //= 10  

    while get_time(level) > limit:
        level += 1
    
    return level
