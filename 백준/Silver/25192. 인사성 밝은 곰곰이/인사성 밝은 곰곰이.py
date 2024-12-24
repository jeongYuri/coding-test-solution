import math
import sys
input = sys.stdin.readline
n = int(input())
people = set()
cnt = 0
for _ in range(n):
    text = input().rstrip()
    if text=='ENTER':
        people.clear()
    elif text not in people:
        people.add(text)
        cnt +=1
print(cnt)