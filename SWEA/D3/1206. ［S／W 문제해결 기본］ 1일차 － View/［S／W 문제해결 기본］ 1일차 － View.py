t = 10
for tc in range(1,t+1):
    count = int(input())
    building = list(map(int,input().split()))
    ans = 0
    for i in range(2,count-2):
        heights = [building[i - 2], building[i - 1], building[i + 1], building[i + 2]]
        if building[i] > max(heights):
            ans += building[i] - max(heights)
    print(f'#{tc} {ans}')
