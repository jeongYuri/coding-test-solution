from itertools import permutations,combinations
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    numbers = ''.join(map(str, numbers))
    sosu = set()
    for i in range(1, len(numbers) + 1):
        combi = permutations(numbers, i)
        for p in combi:
            num = int(''.join(p))
            if is_prime(num):
                sosu.add(num)

    answer = len(sosu)
    return answer
    