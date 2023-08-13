def solution(keymap, targets):
    answer = []
    for word in targets:
        count = 0
        for char in word:
            cnt = 101
            flag = False
            for key in keymap:
                if char in key:
                    cnt = min(key.index(char)+1,cnt)
                    flag = True
            if not flag:
                count = -1;
                break
            count += cnt
        answer.append(count)
    return answer