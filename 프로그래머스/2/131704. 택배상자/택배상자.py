def solution(order):
    st = []
    idx, num = 0,0
    n = len(order)
    while idx<n:
        if order[idx]>num:
            num+=1
            st.append(num)
        elif st[-1]==order[idx]:
            st.pop()
            idx+=1
        else:
            return idx
    return idx