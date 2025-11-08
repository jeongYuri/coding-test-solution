def solution(ingredient):
    answer = 0
    st = []
    for ham in ingredient:
        st.append(ham)
        if st[-4:]==[1,2,3,1]:
            answer+=1
            del st[-4:]
    return answer