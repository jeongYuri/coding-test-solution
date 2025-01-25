import sys
input = sys.stdin.readline

alpha = {
    'A':3, 'B':2, 'C':1, 'D':2, 'E':3, 'F':3, 'G':2, 'H':3, 'I':3, 'J':2,
    'K':2, 'L':1, 'M':2, 'N':2, 'O':1, 'P':2, 'Q':2, 'R':2, 'S':1, 'T':2,
    'U':1, 'V':1, 'W':1, 'X':2, 'Y':2, 'Z':1
}
a = list(input().strip())
b = list(input().strip())

combi = []
for x,y in zip(a,b):
    combi.append(alpha[x])
    combi.append(alpha[y])

if len(a) > len(b):
    for x in a[len(b):]:
        combi.append(alpha[x])
elif len(b) > len(a):
    for x in b[len(a):]:
        combi.append(alpha[x])

while len(combi) > 2:
    temp = []
    for i in range(len(combi) - 1):
        temp.append((combi[i] + combi[i+1]) % 10)
    combi = temp

print(f"{combi[0]}{combi[1]}")