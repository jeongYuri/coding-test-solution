def solution(s):
    answer = []
    s = s[2:-2].replace("}","").replace(","," ").split("{")
    for i, v in enumerate(s):
        s[i] = v.split()
    s.sort(key = lambda x:len(x))
    for i in s:
        for j in range(len(i)):
            if int(i[j]) not in answer:
                answer.append(int(i[j]) )
    return answer
