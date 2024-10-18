def solution(record):
    answer = []
    user_dict = {}
    for r in record:
        parts = r.split(" ")
        if len(parts) < 2:
            continue  
        state = parts[0]
        ids = parts[1]

        if state in ['Enter', 'Change']:
            name = parts[2]
            user_dict[ids] = name
    for r in record:
        parts = r.split(" ")
        state = parts[0]
        ids = parts[1]

        if state == 'Enter':
            answer.append(f"{user_dict[ids]}님이 들어왔습니다.")
        elif state == 'Leave':
            answer.append(f"{user_dict[ids]}님이 나갔습니다.")

    return answer