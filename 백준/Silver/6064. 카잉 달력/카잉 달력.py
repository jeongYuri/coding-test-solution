import math

def calendars(n, m, x, y):
    g = math.gcd(n, m)
    lcm = (n * m) // g

    for k in range(x, lcm + 1, n):
        if (k - 1) % m + 1 == y:
            return k
    return -1

tc = int(input())
for _ in range(tc):
    n, m, x, y = map(int, input().split())
    result = calendars(n, m, x, y)
    print(result)
