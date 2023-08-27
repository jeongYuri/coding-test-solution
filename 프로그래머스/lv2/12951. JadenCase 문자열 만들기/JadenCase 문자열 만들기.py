def solution(s):
    s = s.split(' ')
    for i, word in enumerate(s):
       
        s[i] = word[:1].upper()+word[1:].lower()
            
    return ' '.join(s)