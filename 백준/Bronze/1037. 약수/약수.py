import sys
input = sys.stdin.readline
def find_n(nums):
    return min(nums)*max(nums)
n = int(input())
nums= list(map(int,input().split()))
ans = find_n(nums)
print(ans)

