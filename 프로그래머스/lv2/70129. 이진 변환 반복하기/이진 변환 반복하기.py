def solution(s):
    answer = []
    delete = 0
    count = 0
    while s!="1":
        new = ""
        for i in s:
            if i!="0":
                new +=i
            else:
                delete +=1
        count +=1
        s = bin(len(new))[2:]
    answer.append(count)
    answer.append(delete)
    return answer