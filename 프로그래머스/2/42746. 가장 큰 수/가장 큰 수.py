def solution(numbers):
    answer = ''
    big_num = [str(n) for n in numbers]
    big_num.sort(key = lambda n:n*3,reverse = True)
    return str(int(''.join(big_num)))