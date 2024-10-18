from itertools import combinations
from collections import Counter
def solution(orders, course):
    ans = []
    for c in course:
        combo = []
        for order in orders:
            so = sorted(order)
            combo.extend(combinations(so,c))
        combo_cnt = Counter(combo)
        if combo_cnt:
            max_cnt = max(combo_cnt.values())
            if max_cnt>=2:
                for combo,cnt in combo_cnt.items():
                    if cnt==max_cnt:
                        ans.append(''.join(combo))
    return sorted(ans)