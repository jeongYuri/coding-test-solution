import re
import sys
input = sys.stdin.readline

n = int(input())
res = []
for _ in range(n):
    word = input().strip()
    numbers = re.findall(r"\d+",word)
    res.extend([str(int(num)) for num in numbers])

res.sort(key = lambda x:int(x))
for r in res:
    print(r)