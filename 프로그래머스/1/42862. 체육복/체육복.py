def solution(n, lost, reserve):
    reserve_s = set(reserve)-set(lost)
    lost_s = set(lost)-set(reserve)
    
    for r in sorted(reserve_s):
        if r-1 in lost_s:
            lost_s.remove(r-1)
        elif r+1 in lost_s:
            lost_s.remove(r+1)
    return n-len(lost_s)
            