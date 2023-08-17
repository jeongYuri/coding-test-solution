def solution(my_strings, parts):
    answer = ''
    for index, part in enumerate(parts):
        s,e = parts[index][0],parts[index][1]
        answer+=my_strings[index][s:e+1]
    return answer