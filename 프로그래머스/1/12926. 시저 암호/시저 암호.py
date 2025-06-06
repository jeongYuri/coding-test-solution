from string import ascii_lowercase
from string import ascii_uppercase

def solution(s, n):
    answer = ''
    lowercase= list(ascii_lowercase)*2
    uppercase= list(ascii_uppercase)*2
    for i in s:
        if i in lowercase:
            answer+= lowercase[lowercase.index(i)+n]
        elif i in uppercase:
            answer +=uppercase[uppercase.index(i)+n]
        else:answer +=" "
    return answer