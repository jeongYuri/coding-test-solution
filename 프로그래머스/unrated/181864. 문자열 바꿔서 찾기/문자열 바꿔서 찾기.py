def solution(myString, pat):
    anser=[]
    for i in myString:
        if i=='A':
            a = i.replace(i,'B')
            anser.append(a)
        elif i=='B':
            b = i.replace(i,'A')
            anser.append(b)
    if pat in ''.join(anser):
        return 1
    else:
        return 0
