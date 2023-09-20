def solution(s):
    answer = []
    s = s[2:-2].replace("{","").replace(","," ").split("}")
    for i, v in enumerate(s):
        s[i] = v.split()
    s.sort(key = lambda x:len(x))
    for tu in s:
        dif = set(tu) - set(answer)
        answer.append(list(dif)[0])
    answer = [int(i) for i in answer] 
    return answer
       

           
