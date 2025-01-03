import sys
input = sys.stdin.readline
def cut(a,n):
    if n==1:
        return
    for i in range(a+n//3,a+(n//3)*2):
        res[i]=' '
    cut(a,n//3) #왼쪽 잘라나가기
    cut(a+n//3*2,n//3)#오른쪽 잘라나가기
while True:
    try:
        n = int(input())
        res = ['-']*(3**n)
        cut(0,3**n)
        print(''.join(res))
    except:
        break

