import sys
input = sys.stdin.readline

n = int(input())
tasty = [list(map(int, input().split())) for _ in range(n)]

min_diff = float('inf') #최소 차이를 저장할 변수

for i in range(1,1<<n):
    sour = 1
    bitter = 0

    for j in range(n):
        if i&(1<<j):
            sour *= tasty[j][0]
            bitter += tasty[j][1]
    min_diff = min(min_diff, abs(sour-bitter))
print(min_diff)
