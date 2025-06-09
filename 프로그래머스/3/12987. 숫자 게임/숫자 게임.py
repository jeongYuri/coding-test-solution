def solution(A, B):
    A.sort()
    B.sort()
    score = 0
    a_index, b_index = 0,0
    while a_index<len(A) and b_index<len(B):
        if A[a_index]<B[b_index]:
            score +=1
            a_index +=1
            b_index +=1
        else:
            b_index +=1
    return score