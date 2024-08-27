import sys
input = sys.stdin.readline

nums = map(int, input().split())
ans = sum(x * x for x in nums) % 10

print(ans)