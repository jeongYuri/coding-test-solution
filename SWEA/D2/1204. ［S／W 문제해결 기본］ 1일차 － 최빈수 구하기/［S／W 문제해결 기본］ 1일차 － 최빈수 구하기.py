from collections import Counter
t = int(input())
for tc in range(1,t+1):
    n = int(input())
    score = list(map(int,input().split()))
    score_count = Counter(score)
    max_count = max(score_count.values())

    max_numbers = [num for num, count in score_count.items() if count == max_count]

    print(f'#{tc} {max_numbers[0]}')
