from itertools import permutations
def solution(k, dungeons):
    answer = 0
    alld = []
    for i in permutations(dungeons,len(dungeons)):
        alld.append(i)
    i = 0
    possible = []
    while i<len(alld):
        count = 0
        stamina = k
        for j in alld[i]:
            if stamina >= j[0]:
                count +=1
                stamina -= j[1]
            else:
                break
        possible.append(count)
        i+=1
    answer = max(possible)
    return answer