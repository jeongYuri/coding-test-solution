def solution(ingredient):
    count = 0
    hab = []
    for i in ingredient:
        hab.append(i)
        if hab[-4:]==[1,2,3,1]:
            count +=1
            for _ in range(4):
                hab.pop()
    return count