def solution(rank, attendance):
    answer = []
    student = sorted([(r,i) for i,r in enumerate(rank)])   
    for r,i in student:
        if attendance[i]:
            answer.append(i)
            if len(answer)==3:
                break
    return answer[0]*10000+answer[1]*100+answer[2]