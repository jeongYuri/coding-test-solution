from collections import Counter
def solution(clothes):
    ans = 1
    closet = Counter([kind for name, kind in clothes])
    for count in closet.values():
        ans *= (count+1)
    return ans-1