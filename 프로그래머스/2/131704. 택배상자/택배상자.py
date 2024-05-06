def solution(order):
    answer = 0
    box = []
    i = 1
    while i != len(order)+1:
        box.append(i)
        while box[-1] == order[answer]:
            answer +=1
            box.pop()
            if len(box)==0:
                break
        i+=1
        
    return answer