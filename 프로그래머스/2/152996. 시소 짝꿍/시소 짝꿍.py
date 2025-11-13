from collections import defaultdict
def solution(weights):
    ans = 0
    cnt = defaultdict(int)
    ratios = [1, 2/3, 3/2, 1/2, 2, 3/4, 4/3]
    for w in weights:
        for r in ratios:
            target = w*r
            if target in cnt:
                ans+= cnt[target]
        cnt[w]+=1
        
    return ans