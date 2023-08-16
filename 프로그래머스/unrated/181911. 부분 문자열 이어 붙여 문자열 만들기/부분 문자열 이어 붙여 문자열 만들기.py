def solution(my_strings, parts):
    answer = ''
    for a,b in enumerate(parts):
        s, e = parts[a][0],parts[a][1]
        answer += my_strings[a][s:e+1]
    return answer