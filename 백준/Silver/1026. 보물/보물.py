import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort()
b.sort(reverse= True)
sums = sum(x * y for x, y in zip(a, b))
print(sums)

