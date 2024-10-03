import sys
input = sys.stdin.readline

n = int(input())
scores = list(map(int, input().split()))
ans = 0
current = 0
for i in range(n):
    if scores[i]==1:
        current +=1
        ans += current
    else:
        current  = 0
print(ans)