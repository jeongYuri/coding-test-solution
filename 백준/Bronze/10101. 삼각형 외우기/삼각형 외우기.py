import sys
input = sys.stdin.readline

angles = [int(input()) for _ in range(3)]

if angles.count(60) == 3:
    print('Equilateral')
elif sum(angles) == 180:
    if len(set(angles)) == 2:
        print('Isosceles')
    elif len(set(angles)) == 3:
        print('Scalene')
else:
    print('Error')






