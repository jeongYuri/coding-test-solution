def solution(rank, attendance):
    answer = []
    student = sorted([(r,i) for i,r in enumerate(rank) if attendance[i]])   
    
    return student[0][1]*10000+student[1][1]*100+student[2][1]