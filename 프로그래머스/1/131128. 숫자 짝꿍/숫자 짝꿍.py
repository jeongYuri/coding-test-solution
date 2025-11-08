from collections import Counter

def solution(X, Y):
    ans = []
    cntX = Counter(X)
    cntY = Counter(Y)
    
    for num in range(9,-1,-1):
        num = str(num)
        if num in cntX and num in cntY:
            ans.append(num*min(cntX[num],cntY[num]))
    ans = ''.join(ans)
    if ans=='':
        return '-1'
    elif ans[0]=='0':
        return '0'
    else:
        return ans
    return answer