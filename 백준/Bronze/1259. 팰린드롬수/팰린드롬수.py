import sys
input = sys.stdin.readline
def check(n):
    s = str(n)
    return s==s[::-1]
while True:
    try:
        n = int(input().strip())
        if n==0:
            break
        if check(n):
            print('yes')
        else:
            print('no')
    except EOFError:
        break