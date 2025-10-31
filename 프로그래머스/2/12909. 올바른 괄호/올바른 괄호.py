def solution(s):
    st = []
    for ch in s:
        if ch=='(':
            st.append(ch)
        else:
            if not st:
                return False
            st.pop()
    return len(st) == 0 
        