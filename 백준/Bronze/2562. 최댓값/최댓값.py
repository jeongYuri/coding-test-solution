import sys
input = sys.stdin.readline
number = []
for i in range(9):
    number.append(int(input().rstrip()))
print(max(number))
print(number.index(max(number))+1)
