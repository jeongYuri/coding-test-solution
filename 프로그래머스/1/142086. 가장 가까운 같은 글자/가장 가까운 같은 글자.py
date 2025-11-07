def solution(s):
    answer = []
    last_idx = {}
    for i,ch in enumerate(s):
        if ch not in last_idx:
            answer.append(-1)
        else:
            answer.append(i-last_idx[ch])
        last_idx[ch] = i
    return answer