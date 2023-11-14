for tc in range(1, 11):
    count = int(input())
    box = list(map(int, input().split()))

    for i in range(count):
        box[box.index(max(box))] -= 1
        box[box.index(min(box))] += 1

    answer = max(box) - min(box)
    print(f'#{tc} {answer}')