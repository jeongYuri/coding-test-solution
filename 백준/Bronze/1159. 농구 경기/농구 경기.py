import sys
input = sys.stdin.readline

n = int(input())
player = [input().strip() for _ in range(n)]
cnt = {}
for name in player:
    if name[0] not in cnt:
        cnt[name[0]] = 1
    elif name[0] in cnt:
        cnt[name[0]]+=1
ans = []
for first, count in cnt.items():
    if count>=5:
        ans.append(first)
if ans:
    print(''.join(sorted(ans)))
else:
    print("PREDAJA")