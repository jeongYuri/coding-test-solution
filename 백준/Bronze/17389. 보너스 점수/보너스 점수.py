import sys
input = sys.stdin.readline

t = int(input())
score = list(str(input()))
res = 0
bonus = 0
for i in range(t):
    if score[i]=='X':
        bonus = 0
    elif score[i]=='O' and score[i-1]=='X':
        res += i+1
        bonus=1
    else:
        res+=i+1+bonus
        bonus += 1
print(res)


