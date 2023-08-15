def solution(num_list):
    hol=[]
    su=[]
    for i in num_list:
        if i%2!=0:
            hol.append(str(i))
        else:
            su.append(str(i))
    return int(''.join(hol))+int(''.join(su))