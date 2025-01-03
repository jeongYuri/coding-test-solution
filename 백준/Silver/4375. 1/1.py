import sys
input = sys.stdin.readline

while True:
    try:
        n = int(input().strip())
    except:
        break
    remainder = 1  
    cnt = 1  
    while remainder % n != 0:
        remainder = (remainder * 10 + 1) % n 
        cnt += 1

    print(cnt)
