t = int(input())
for tc in range(1,t+1):
    score = (list(map(int,input().split())))
    score.sort(reverse = True)
    hab = 0
    socre_avg = 0
    for i in range(1,9):
        hab += score[i]
        socre_avg = round(hab/8)

    print(f'#{tc} {socre_avg}')