from collections import defaultdict
def solution(n, results):
    answer = 0
    winner = defaultdict(set) 
    looser = defaultdict(set) 
    for win,lose in results:
        winner[lose].add(win)
        looser[win].add(lose)
    for i in range(n+1):
        for win in winner[i]:
            looser[win].update(looser[i])
        for lose in looser[i]:
            winner[lose].update(winner[i])
    for i in range(1,n+1):
        if len(winner[i]) + len(looser[i]) == n-1:  
            answer += 1

    return answer