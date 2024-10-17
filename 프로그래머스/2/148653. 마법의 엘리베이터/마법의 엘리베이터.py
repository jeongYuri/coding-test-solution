def solution(storey):
    cnt = 0
    while storey>0:
        digit = storey%10
        if digit > 5 or(digit==5 and (storey//10)%10>4):
            cnt += 10-digit
            storey+=10
        else:
            cnt +=digit
        storey//=10
    return cnt