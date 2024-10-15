def solution(participant, completion):
    ans = ''
    participant.sort()
    completion.sort()
    hash = {}
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            ans = participant[i]
            break
        else:
            ans = participant[-1]
    if ans == '':
        ans = participant[-1]
    return ans