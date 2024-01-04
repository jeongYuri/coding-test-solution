import sys
from collections import Counter

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    text = input().strip()
    front, back = 0,len(text)-1
    check = 0

    for _ in range(len(text)):
        if front>=back:
            break
        if text[front]==text[back]:
            front +=1
            back-=1
            continue
        if text[front]==text[back-1]:
            temp = text[front:back]
            if temp[:]==temp[::-1]:
                check = 1
                break
        if text[front+1]==text[back]:
            temp = text[front+1:back+1]
            if temp[:]==temp[::-1]:
                check =1
                break
        check =2
        break
    print(check)