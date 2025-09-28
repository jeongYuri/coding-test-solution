import sys
import math
input = sys.stdin.readline

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(math.isqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def is_palindrome(x):
    s = str(x)
    return s == s[::-1]

n = int(input())
while True:
    if is_prime(n) and is_palindrome(n):
        print(n)
        break
    n += 1
