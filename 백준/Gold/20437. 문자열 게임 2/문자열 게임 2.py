import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    w = input().rstrip()
    k = int(input())
    cnt_dict = {}

    # 각 문자 개수 세기
    for char in w:
        cnt_dict[char] = cnt_dict.get(char, 0) + 1

    check = False
    max_ans = -1
    min_ans = float('inf')  # 큰 값으로 초기화

    check_dict = {}

    # k번 이상 등장하는 문자들의 인덱스 저장
    for i in range(len(w)):
        if cnt_dict[w[i]] < k:
            continue
        check = True
        if w[i] not in check_dict:
            check_dict[w[i]] = []
        check_dict[w[i]].append(i)

    #최소, 최대 길이 계산
    for key, v in check_dict.items():
        if len(v) >= k:
            for i in range(len(v) - k + 1):
                length = v[i + k - 1] - v[i] + 1
                max_ans = max(max_ans, length)
                min_ans = min(min_ans, length)

    if check:
        print(min_ans, max_ans)
    else:
        print(-1)
