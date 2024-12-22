import sys
input = sys.stdin.readline

n = int(input())
arr = set(map(int, input().split()))
arr = sorted(arr)
print(*arr)




