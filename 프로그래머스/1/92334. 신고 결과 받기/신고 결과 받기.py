from collections import defaultdict
def solution(id_list, report, k):
    report = list(set(report))#중복 없이
    users = defaultdict(set)
    count = defaultdict(int)
    answer = []
    
    for r in report:
        name, value = r.split(' ')
        users[name].add(value)
        count[value] +=1
    for i in id_list:
        result = 0
        for u in users[i]:
            if count[u]>=k:
                result +=1
        answer.append(result)
    return answer