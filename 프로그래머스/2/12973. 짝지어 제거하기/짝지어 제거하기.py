def solution(s):
    st = []
    for ch in s:
        if st and st[-1]==ch:
            st.pop()
        else:
            st.append(ch)
    if not st:
        return 1
    else:
        return 0
        