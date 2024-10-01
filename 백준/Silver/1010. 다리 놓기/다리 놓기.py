def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def combination(n, r):
    return factorial(n) / (factorial(n - r) * factorial(r))

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(int(combination(M, N)))