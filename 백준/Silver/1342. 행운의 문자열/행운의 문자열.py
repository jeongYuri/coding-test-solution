import sys
from collections import Counter
input = sys.stdin.readline

def backtrack(path, counter, prev_char):
    if len(path) == total_len:
        global res
        res +=1
        return
    for char in counter:
        if counter[char]>0 and char!= prev_char:
            counter[char] -=1
            backtrack(path+char, counter, char)
            counter[char]+=1

s = input().strip()
counter = Counter(s)
total_len  = len(s)
res = 0

backtrack("",counter,"")
print(res)
