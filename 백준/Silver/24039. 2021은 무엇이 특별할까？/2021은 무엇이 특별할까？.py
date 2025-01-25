def sieve(max_num):
    primes = [True] * (max_num + 1)
    primes[0] = primes[1] = False  
    for i in range(2, int(max_num ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_num + 1, i):
                primes[j] = False
    return [x for x in range(max_num + 1) if primes[x]]


def find_special(num):
    max_num = 10 ** 6 
    prime_list = sieve(max_num)

    for i in range(len(prime_list) - 1):
        prod = prime_list[i] * prime_list[i + 1]
        if prod > num:
            return prod

n = int(input())
print(find_special(n))