import sys
from collections import defaultdict
input = sys.stdin.readline

n,m = map(int,input().split())
eng = defaultdict(int)
cnt = 0
for _ in range(n):
    word = input().rstrip()
    eng[word]+=1
eng = (sorted(eng.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))
for word, cnt in eng:
    if(len(word))>=m:
        print(word)