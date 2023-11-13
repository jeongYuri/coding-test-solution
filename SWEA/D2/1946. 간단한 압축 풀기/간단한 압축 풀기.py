t = int(input())
for tc in range(1,t+1):
    n = int(input())
    word = ""
    text = []
    count = 0
    for num in range(1,n+1):
        al, cnt = map(str, input().split())
        word += al *int(cnt)
    print(f'#{tc}')
    for i in range(len(word)):
        if (i+1)%10==0:
            print(word[i])
        else:
            print(word[i],end="")
    print()
