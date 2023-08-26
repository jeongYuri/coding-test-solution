def solution(ingredient):
    count = 0
    ham = []
    for h in ingredient:
        ham.append(h)
        if ham[-4:]==[1,2,3,1]:
            count +=1
            for _ in range(4):
                ham.pop()
    return count