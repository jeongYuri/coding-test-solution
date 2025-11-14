from itertools import combinations
from collections import Counter
def solution(orders, course):
    ans = []
    orders = [''.join(sorted(o)) for o in orders]
    for c in course:
        com_list = []
        for order in orders:
            if len(order)>=c:
                com_list+=combinations(order,c)
        cnt = Counter(com_list)
        if not cnt:
            continue
        max_cnt = max(cnt.values())
        if max_cnt<2:
            continue
        for k, v in cnt.items():
            if v==max_cnt:
                ans.append(''.join(k))
        
    return sorted(ans)