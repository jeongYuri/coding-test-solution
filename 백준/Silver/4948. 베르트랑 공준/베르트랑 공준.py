import sys
import math
def sieve(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(math.sqrt(limit)) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False
    return primes

primes = sieve(123456 * 2)
for line in sys.stdin:
    n = int(line.strip())
    if n == 0:
        break
    print(sum(primes[n+1:2*n+1]))