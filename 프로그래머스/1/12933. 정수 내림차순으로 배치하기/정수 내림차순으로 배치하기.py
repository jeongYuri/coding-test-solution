def solution(n):
    answer = [int(digit) for digit in str(n)]
    answer.sort(reverse = True)
    
    return int(''.join(map(str, answer))) 