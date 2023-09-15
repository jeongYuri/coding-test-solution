import math
def lcm(a,b):
    return int(a*b/math.gcd(a,b))

def solution(arr):
    st = []
    for ar in arr:
        if not st:
            st.append(ar)
        else:
            st.append(lcm(st.pop(),ar))
    return st[-1]