def solution(numbers):
    answer = ''
    bigsu = [str(p) for p in numbers]
    bigsu.sort(key = lambda p:p*3,reverse = True)
    return str(int(''.join(bigsu)))