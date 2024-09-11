import sys
input = sys.stdin.readline
me = input().rstrip()
doctor = input().rstrip()

if doctor in me :
    print('go')
else:
    print('no')