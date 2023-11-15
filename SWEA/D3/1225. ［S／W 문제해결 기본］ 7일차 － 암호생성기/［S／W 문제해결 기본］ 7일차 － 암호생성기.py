for tc in range(1,11):
    n = int(input())
    array = list(map(int,input().split()))
    i = 1
    while True:
        if i>5:
            i = 1
        t = array.pop(0)-i
        if t<=0:
            array.append(0)
            break
        array.append(t)
        i+=1
    answer = ' '.join(map(str,array))
    print(f'#{tc} {answer}')