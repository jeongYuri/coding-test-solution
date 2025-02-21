
import sys
input = sys.stdin.readline
def triangle_area(x1, y1, x2, y2, x3, y3):
    return abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2


for line in sys.stdin:
    nums = list(map(float, line.split()))
    if len(nums) != 12:
        continue
    if all(n == 0.0 for n in nums):
        break

    x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6 = nums

    T = triangle_area(x4, y4, x5, y5, x6, y6)

    cross = abs((x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1))
    if cross == 0:
        continue

    k = T / cross

    x7 = x1 + k * (x3 - x1)
    y7 = y1 + k * (y3 - y1)
    x8 = x2 + k * (x3 - x1)
    y8 = y2 + k * (y3 - y1)

    print(f"{x8:.3f} {y8:.3f} {x7:.3f} {y7:.3f}")

