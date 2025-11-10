def solution(n, words):
    answer = []
    prev = []
    for i in range(len(words)):
        if not prev:
            prev.append(words[i])
            continue
        prev_w = prev[-1]
        curr_w = words[i]
        if curr_w in prev or prev_w[-1] != curr_w[0]:
            
            person = (i % n) + 1
            turn = (i // n) + 1
            return [person, turn]

        prev.append(curr_w)

    return [0, 0]