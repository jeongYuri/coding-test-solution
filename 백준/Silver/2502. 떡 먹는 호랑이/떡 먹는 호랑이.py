import sys
input = sys.stdin.readline

D, K = map(int, input().split())

a = [0] * (D+1)
b = [0] * (D+1)
a[1], b[1] = 1, 0
a[2], b[2] = 0, 1

for i in range(3, D+1):
    a[i] = a[i-1] + a[i-2]
    b[i] = b[i-1] + b[i-2]

for A in range(1, K):
    if (K - a[D]*A) % b[D] == 0:
        B = (K - a[D]*A) // b[D]
        if A <= B:
            print(A)
            print(B)
            break
