def solution(new_id):
    answer = ''
    new_id = new_id.lower() #1단계
    for w in new_id:
        if w.isalpha() or w.isdigit() or w in ['-', '_', '.']: #2단계
            answer += w
    while '..'in answer:
         answer = answer.replace('..','.')
    if answer[0]=='.':
        if len(answer)>1:
            answer = answer[1:]
    if answer[-1]=='.':    
        answer = answer[:-1]
    if len(answer)==0:
        answer +='a'
    if len(answer)>=16:
        answer = answer[:15]
        if answer[-1]=='.':
             answer = answer[:-1]
    while len(answer)<3:
        answer += answer[-1]
    return answer

   