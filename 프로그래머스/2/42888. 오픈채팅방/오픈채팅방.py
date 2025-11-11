def solution(record):
    answer = []
    user = {}
    for re in record:
        parts = re.split()
        state = parts[0]
        uid= parts[1]
        if state in ('Enter','Change'):
            nickname = parts[2]
            user[uid] = nickname
    
    for re in record:
        parts = re.split()
        state = parts[0]
        uid = parts[1]
        if state == 'Enter':
            answer.append(f"{user[uid]}님이 들어왔습니다.")
        elif state == 'Leave':
            answer.append(f"{user[uid]}님이 나갔습니다.")

    return answer