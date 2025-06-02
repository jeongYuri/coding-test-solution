import sys
input = sys.stdin.readline
def check(num):
    seen = [False]*10
    while(num>0):
        digit = num %10
        if seen[digit]:
            return True
        seen[digit] = True
        num//=10
    return False

while True:
    line = input().strip()
    if not line: 
        break
    n, m = map(int, line.split())
    cnt = 0
    for i in range(n,m+1):
        if not check(i):
            cnt+=1

    print(cnt)




