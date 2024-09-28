import re
import sys
input = sys.stdin.readline

s = input().rstrip()
group = re.findall(r'(0+|1+)',s)
cnt = {0: 0, 1: 0}
for g in group:
    if '1' in g:
        cnt[1]+=1
    else:
        cnt[0]+=1

print(min(cnt.values()))
