import sys
input = sys.stdin.readline

n = int(input())
command= list(input().strip() for _ in range(n))
pre = []
for co in command:
    flag = False
    words = co.split()
    for i, word in enumerate(words):
        if word[0].upper() not in pre:
            pre.append(word[0].upper())
            words[i] = '[' + word[0] +']' + word[1:]
            print(' '.join(words))
            flag = True
            break
    if not flag:
        for i in range(len(co)):
            ch = co[i]
            if ch==' ':
                continue
            if ch.upper() not in pre:
                pre.append(ch.upper())
                co = co[:i] + '[' + ch + ']' + co[i + 1:]
                break
        print(co)