def solution(new_id):
    new_id = new_id.lower()
    answer = ''
    for ch in new_id:
        if ch.isalnum() or ch in ['-','_','.']:
            answer += ch
    while '..' in answer:
        answer = answer.replace('..', '.')
 
    if answer.startswith('.'):
        answer = answer[1:]
    if answer.endswith('.'):
        answer = answer[:-1]
    
  
    if answer == '':
        answer = 'a'
    
   
    if len(answer) >= 16:
        answer = answer[:15]
        if answer.endswith('.'):
            answer = answer[:-1]
   
    while len(answer) < 3:
        answer += answer[-1]
    
    return answer
