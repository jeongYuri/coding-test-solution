from collections import defaultdict
def solution(id_list, report, k):
    answer = []
    report = list(set(report))
    count = defaultdict(int)
    user = defaultdict(set) #중복 제거
    
    for r in report:
        name, values = r.split(' ')
        user[name].add(values)
        count[values] +=1
        
    for i in id_list:
        result = 0
        for u in user[i]:
            if count[u]>=k:
                result +=1
        answer.append(result)
    return answer
   