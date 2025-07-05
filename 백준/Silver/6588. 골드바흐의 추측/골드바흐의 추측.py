import sys
input = sys.stdin.readline

MAX = 1000000
is_prime = [True] * (MAX + 1)
is_prime[0] = is_prime[1] = False
prime_list = []

for i in range(2, MAX + 1):
    if is_prime[i]:
        prime_list.append(i)
        for j in range(i * 2, MAX + 1, i):
            is_prime[j] = False

while True:
    n = int(input())
    if n == 0:
        break

    found = False
    for a in prime_list:
        if a > n // 2:
            break
        b = n - a
        if is_prime[b]:
            print(f"{n} = {a} + {b}")
            found = True
            break

    if not found:
        print("Goldbach's conjecture is wrong.")
