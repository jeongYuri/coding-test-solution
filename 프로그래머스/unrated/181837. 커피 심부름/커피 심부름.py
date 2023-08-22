def solution(order):
    cost = 0
    for cof in order:
        if  "americano" in cof or "anything" in cof:
            cost +=4500
        elif "cafelatte" in cof:
            cost +=5000
    return cost