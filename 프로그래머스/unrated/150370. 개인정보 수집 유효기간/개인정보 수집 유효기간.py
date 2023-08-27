def solution(today, terms, privacies):
    answer = []
    idx = 1
    today_y, today_m, today_d = map(int, today.split('.'))
    terms_dic = dict()
    
    for t in terms:
        alp, num = t.split(' ')
        terms_dic[alp] = int(num)
    terms_alp = list(terms_dic.keys())
    
    for p in privacies:
        days, alpa = p.split(' ')
        year, month, day = map(int, days.split('.'))
        
        for alp in terms_alp:
            if alp==alpa:
                month += terms_dic[alp]
                while True:
                    if month>12:
                        year +=1
                        month = month -12
                    else:
                        break
        if today_y>year:
            answer.append(idx)
        elif (today_y == year) and (today_m>month):
            answer.append(idx)
        elif (today_y==year) and (today_m == month) and (today_d>=day):
            answer.append(idx)
        idx +=1
    return answer