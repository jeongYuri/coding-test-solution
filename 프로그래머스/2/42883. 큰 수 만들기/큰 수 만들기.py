def solution(number, k):
    st = []
    for num in number:
        while k and st and st[-1]<num:
            st.pop()
            k-=1
        st.append(num)
    st = st[:-k] if k else st
    return ''.join(st)