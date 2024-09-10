MOD = 10 ** 9 + 7

def matrix_mult(A, B):
    return [
        [
            (A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD,
            (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD
        ],
        [
            (A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD,
            (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD
        ]
    ]

def matrix_pow(mat, n):
    result = [[1, 0], [0, 1]] 
    base = mat

    while n > 0:
        if n % 2 == 1:
            result = matrix_mult(result, base)
        base = matrix_mult(base, base)
        n //= 2

    return result

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    fib_matrix = [[1, 1], [1, 0]]
    result_matrix = matrix_pow(fib_matrix, n-1)
    return result_matrix[0][0]

import sys
input = sys.stdin.read
n = int(input().strip())
print(fibonacci(n))
