import sys
input = sys.stdin.readline

def scalar_minimum(t, tc):
    results = []

    for idx, value in enumerate(tc, 1):
        n, v1, v2 = value
        v1.sort()
        v2.sort(reverse=True)
        min_scalar = sum(v1[i] * v2[i] for i in range(n))
        results.append(f"Case #{idx}: {min_scalar}")

    return results

t = int(input())
tc = []
for _ in range(t):
    n = int(input())
    v1 = list(map(int, input().split()))
    v2 = list(map(int, input().split()))
    tc.append((n, v1, v2))

res = scalar_minimum(t, tc)
for result in res:
    print(result)