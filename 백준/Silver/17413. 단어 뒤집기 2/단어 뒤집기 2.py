import sys
input = sys.stdin.readline
s = input().rstrip()
res = ''
temp = ''
in_tag = False
for i in s:
    if i == '<':
        if temp:
            res += temp[::-1]
            temp = ''
        in_tag = True
        res += i
    elif i == '>':
        in_tag = False
        res += i
    elif in_tag:
        res += i
    else:
        if i == ' ' and temp:
            res += temp[::-1] + ' '
            temp = ''
        else:
            temp += i

if temp:
    res += temp[::-1]

print(res)
