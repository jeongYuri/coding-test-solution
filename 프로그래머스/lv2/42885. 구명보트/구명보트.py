def solution(people, limit):
    count = 0
    i = 0
    j = len(people)-1
    people.sort()
    while i<=j:
        if people[i]+people[j]<=limit:
            count +=1
            i+=1
            j-=1
        else:
            count +=1
            j-=1
    return count
        
        