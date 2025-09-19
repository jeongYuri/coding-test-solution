import sys
input = sys.stdin.readline
from collections import Counter

s = input().strip()
c = Counter(s)
z = c['0']//2
o = c['1']//2
ans = '0'*z + '1'*o
ans = ''.join(sorted(ans))
print(ans)