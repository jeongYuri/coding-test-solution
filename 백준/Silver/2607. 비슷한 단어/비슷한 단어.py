import sys
input = sys.stdin.readline
from collections import Counter
t = int(input())
word = [input().strip() for _ in range(t)]
base =  word[0]
base_cnt= Counter(base)

cnt = 0

for word in word[1:]:
    word_cnt = Counter(word)
    diff = base_cnt-word_cnt
    rev_diff = word_cnt - base_cnt

    total = sum(diff.values())+sum(rev_diff.values())

    if total==0:
        cnt +=1
    elif total ==1:
        cnt+=1
    elif total==2 and len(diff)==1 and len(rev_diff)==1:
        cnt+=1
print(cnt)
