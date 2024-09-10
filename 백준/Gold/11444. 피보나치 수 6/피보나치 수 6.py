MOD = 10**9 + 7

def fib(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = fib(n // 2)
        c = a * ((b * 2) % MOD - a) % MOD  
        d = (a * a % MOD + b * b % MOD) % MOD  
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, (c + d) % MOD)

import sys
input = sys.stdin.read
n = int(input().strip())
print(fib(n)[0])