t = int(input())
for tc in range(1,t+1):
    h1,m1,h2,m2 = map(int,input().split())
    hours = h1 + h2
    minutes = m1+m2

    if hours >= 12:
        hours = hours - 12

    if minutes >= 60:
        hours += minutes // 60
        minutes= minutes-60


    print(f'#{tc} {hours} {minutes}')