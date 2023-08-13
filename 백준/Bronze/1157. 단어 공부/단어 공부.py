import sys
input = sys.stdin.readline
N = input().strip().upper()
ans = {}
for n in N:
    ans[n] = ans.get(n, 0) + 1
max(ans,key=ans.get)
answer = [k for k,v in ans.items() if max(ans.values()) == v]
if len(answer)>1:
  print('?')
else:
  print(''.join(answer))