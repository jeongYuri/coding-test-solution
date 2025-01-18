import sys
from collections import Counter
input = sys.stdin.readline


n,d = map(int,input().split())
num = [i for i in range(1,n+1)]
res = []
for number in num:
    if number >= 10:
        res.extend([int(digit) for digit in str(number)])
    else:
        res.append(number)
cnt = Counter(res)
print(cnt[d])

