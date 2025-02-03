import sys
input = sys.stdin.readline
from itertools import combinations

text = list(input().strip())
indices = []
stk = []
ans = set()

for i in range(len(text)):
    if text[i]=='(':
        stk.append(i)
    elif text[i]==')':
        indices.append((stk.pop(),i))

for i in range(len(indices)):
    for comb in combinations(indices,i+1):
        temp = text[:]
        for idx in comb:
            temp[idx[0]] = temp[idx[1]] = ""
        ans.add("".join(temp))
for item in sorted(list(ans)):
    print(item)

