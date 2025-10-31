def solution(number, k):
    st = []
    for num in number:
        while st and k>0 and st[-1]<num:
            st.pop()
            k-=1
        st.append(num)
    if k>0:
        return ''.join(st[:-k])
    else:
        return ''.join(st)
    