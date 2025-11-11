def convert(n, k):
    s = ''
    while n > 0:
        s = str(n % k) + s
        n //= k
    return s

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def solution(n, k):
    converted = convert(n, k)
    parts = converted.split('0')
    
    count = 0
    for p in parts:
        if p != '' and is_prime(int(p)):
            count += 1
    return count