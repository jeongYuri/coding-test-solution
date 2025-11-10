from collections import Counter
def solution(k, tangerine):
    ans , res = 0,0
    temp  = Counter(tangerine)
    temp = temp.most_common()
    for t in temp:
        res+=t[1]
        ans+=1
        if res>=k:
            return ans
