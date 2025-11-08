def solution(lottos, win_nums):
    answer = []
    zero_c = lottos.count(0)
    cnt = 0
    for lotto in lottos:
        if lotto in win_nums:
            cnt+=1
    best = zero_c + cnt
    worst = cnt
    
    def to_rank(num):
        return 7 - num if num >=2 else 6
    return [to_rank(best), to_rank(worst)]