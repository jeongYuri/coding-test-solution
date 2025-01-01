import sys
input = sys.stdin.readline

a,p = map(int,input().split())
d = []
d.append(a)
while True:
    current = d[-1]
    new_value = sum(int(digit)**p for digit in str(current))
    if new_value in d:
        break
    d.append(new_value)
res = d.index(new_value)
print(res)