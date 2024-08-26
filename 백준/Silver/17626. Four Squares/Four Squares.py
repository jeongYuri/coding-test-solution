import math

def is_square(n):
    return int(math.sqrt(n))**2 == n

def solve(n):
    if is_square(n):
        return 1
    for i in range(1, int(math.sqrt(n)) + 1):
        if is_square(n - i*i):
            return 2
    while n % 4 == 0:  
        n //= 4
    if n % 8 == 7:  
        return 4
    return 3

n = int(input())
print(solve(n))
