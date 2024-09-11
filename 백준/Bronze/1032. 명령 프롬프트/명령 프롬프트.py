import sys
input = sys.stdin.readline

n = int(input())
file = list(input())
for _ in range(n-1):
    other = input()
    for i in range(len(file)):
        if file[i]!=other[i]:
            file[i] = '?'
print(''.join(file))