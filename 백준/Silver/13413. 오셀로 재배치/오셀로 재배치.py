import sys
input = sys.stdin.readline


tc = int(input()) #테스트 데이터 구성
for _ in range(tc):
    n = int(input()) #오셀로 말의 개수
    start = input().strip()
    target = input().strip()

    btow = 0
    wtob = 0

    for i in range(len(start)):
        if start[i]=='B' and target[i] == 'W':
            btow +=1
        elif start[i]== 'W' and target[i] == 'B':
            wtob +=1
    swaps = min(btow,wtob)
    flip = abs(btow-wtob)

    print(swaps+flip)


    cnt = 0


