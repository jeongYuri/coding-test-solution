def solution(topping):
    n = len(topping)
    left = {}
    right = {}
    res = 0
    
    for t in topping:
        right[t] = right.get(t,0)+1
    for t in topping:
        left[t]= left.get(t,0)+1
        right[t] -= 1
        if right[t] == 0:
            del right[t]
        if len(right)==len(left):
            res+=1
        
    return res