def solution(wallet, bill):
    answer = 0
    wallet.sort()
    
    while True:
        if (bill[0] <= wallet[0] and bill[1] <= wallet[1]) or (bill[0] <= wallet[1] and bill[1] <= wallet[0]):
            break
        if bill[0] >= bill[1]:
            bill[0] //= 2
        else:
            bill[1] //= 2
        
        answer += 1
    
    return answer