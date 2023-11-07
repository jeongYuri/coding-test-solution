#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T + 1):
    answer = [ ] 
    N = int(input())
    for i in range(1, N + 1):  # 변경: 범위는 1부터 N까지
        if i % 2 == 0:
            i = i * -1  
        answer.append(i)
    total = sum(answer) 
    print(f'#{tc} {total}')
    # ///////////////////////////////////////////////////////////////////////////////////
