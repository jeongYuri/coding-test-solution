def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])
    limit = -30001
    for route in routes:
        if route[0]>limit:
            answer+=1
            limit = route[1]
    return answer