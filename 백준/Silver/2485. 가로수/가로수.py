import sys
import math
input = sys.stdin.readline

n = int(input())
tree = [(int(input())) for _ in range(n)]
tree.sort()
gaps = [tree[i+1]-tree[i] for i in range(n-1)]
gcd_value = gaps[0]
for gap in gaps[1:]:
    gcd_value = math.gcd(gcd_value,gap)
res = sum((gap//gcd_value)-1 for gap in gaps)


print(res)