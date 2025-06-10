def solution(players, m, k):
    server = []
    
    for now in players:
        total = sum((server + [1])[-k:]) * m
        if total > now:
            server = server + [0]
        else:
            add = (now - total) // m + 1
            server += [add]
    return sum(server)