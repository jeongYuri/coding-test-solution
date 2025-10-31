def solution(price, money, count):
    answer = 0
    want = 0
    for i in range(1,count+1):
        want+= price*i
    if want<money:
        return 0
    else:
        return want-money