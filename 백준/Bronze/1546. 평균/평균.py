import sys
input = sys.stdin.readline

n = int(input())
score = list(map(int,input().split()))
ans = []
max_s = max(score)
for s in score:
    ans.append((s/max_s)*100)
print(sum(ans)/n)
