def solution(num_list):
    hol = 0
    su = 0
    for idx, valuee in enumerate(num_list, start=1):
        if idx % 2==0:
            hol+=valuee
        else:
            su += valuee
    if hol>su:
        return hol
    else:
        return su