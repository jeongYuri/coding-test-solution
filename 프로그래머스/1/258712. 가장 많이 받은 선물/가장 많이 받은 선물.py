def solution(friends, gifts):
    n = len(friends)
    idx = {name: i for i, name in enumerate(friends)}  

    gave = [[0] * n for _ in range(n)]
    
    received = [0] * n

    for gift in gifts:
        a, b = gift.split()
        ai, bi = idx[a], idx[b]
        gave[ai][bi] += 1
        received[bi] += 1

    score = [sum(gave[i]) - received[i] for i in range(n)]

    next_gift = [0] * n

    for i in range(n):
        for j in range(i + 1, n):
            if gave[i][j] > gave[j][i]:
                next_gift[i] += 1
            elif gave[i][j] < gave[j][i]: 
                next_gift[j] += 1
            else:  
                if score[i] > score[j]:
                    next_gift[i] += 1
                elif score[i] < score[j]:
                    next_gift[j] += 1
            
    return max(next_gift)
