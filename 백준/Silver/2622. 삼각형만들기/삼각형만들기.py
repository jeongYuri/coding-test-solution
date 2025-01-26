import sys
input = sys.stdin.readline


def triangles(n):
    count = 0
    for a in range(1, n // 3 + 1):
        start_b = max(a, int((n / 2) - a + 1))
        end_b = (n - a) // 2
        if start_b <= end_b:
            count += (end_b - start_b + 1)

    return count


n = int(input().strip())
print(triangles(n))