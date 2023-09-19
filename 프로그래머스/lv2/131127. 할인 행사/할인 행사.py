def solution(want, number, discount):
    count = 0
    n = len(discount)
    disc = 0
    while disc+10<=n:
        avil = discount[disc:disc+10]
        if all(n==avil.count(w) for w,n in zip(want,number)):
            count +=1
        disc +=1
        
    return count