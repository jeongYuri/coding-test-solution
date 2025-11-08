def solution(survey, choices):
    score = { 'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0 }

    for s, c in zip(survey, choices):
        a, b = s[0], s[1]
        if c < 4:  
            score[a] += 4 - c
        elif c > 4:  
            score[b] += c - 4

    answer = ''
    for left, right in [('R','T'), ('C','F'), ('J','M'), ('A','N')]:
        if score[left] >= score[right]:
            answer += left
        else:
            answer += right

    return answer
