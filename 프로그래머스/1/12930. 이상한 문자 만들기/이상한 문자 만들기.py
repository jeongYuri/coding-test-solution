def solution(s):
    answer = []
    arr = s.split(" ")
    for a in arr:
        tmp = ''
        for i in range(len(a)):
            if i%2==0:
                tmp += a[i].upper()
            else:
                tmp += a[i].lower()
        answer.append(tmp)
    return ' '.join(answer)

