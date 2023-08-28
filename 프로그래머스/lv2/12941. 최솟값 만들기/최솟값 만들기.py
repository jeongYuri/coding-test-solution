def solution(A,B):
    A = sorted(A)
    B = sorted(B,reverse = True)
    hab = 0
    for i,j in zip(A,B):
            hab += i*j
    return hab