import sys
input = sys.stdin.readline
mo = ['a', 'e', 'i', 'o', 'u']
while True:
    word = input().rstrip()
    if word == '#':
        break
    cnt = 0
    word_lower = word.lower()  
    for i in mo:
        cnt += word_lower.count(i)
    print(cnt)