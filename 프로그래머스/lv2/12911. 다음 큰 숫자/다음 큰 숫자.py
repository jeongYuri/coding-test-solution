def solution(n):
    one = bin(n)[2:].count('1')
    i = n+1
    while True:
        if bin(i)[2:].count('1') == one:
                return i
        i +=1
            
            