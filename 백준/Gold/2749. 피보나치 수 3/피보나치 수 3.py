import sys
input = sys.stdin.readline

def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(n):
        a, b = b, (a + b) % 1000000
    return a

n = int(input())
pisano_period = 1500000 
n %= pisano_period

res = fibonacci(n)
print(res)
