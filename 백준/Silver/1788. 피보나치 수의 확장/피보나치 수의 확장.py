import sys
input = sys.stdin.readline

n = int(input().rstrip())
abs_n = abs(n)
fib = [0, 1]
for i in range(2, abs_n + 1):
    fib.append((fib[i - 1] + fib[i - 2]) % 1000000000)
if n == 0:
    print(0)
elif n < 0 and n % 2 == 0:
    print(-1)
else:
    print(1)
print(fib[abs_n])