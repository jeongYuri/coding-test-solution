import sys
input = sys.stdin.readline

score = [(int(input().rstrip())) for _ in range(8)]
ans = []
res = 0
for i in range(5):
    res += max(score)
    ans.append(score.index(max(score))+1)
    score[score.index(max(score))] =-1
ans.sort()
print(res)
print(*ans)