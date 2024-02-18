import sys
input = sys.stdin.readline

text = list(input().rstrip())
dic =  {chr(i): -1 for i in range(ord('a'), ord('z')+1)}
for i in range(len(text)):
    if text[i] in dic:
        if dic[text[i]]==-1:
            dic[text[i]]=i
        else:
            continue


for i in dic.values():
    print(i,end=' ')