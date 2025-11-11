def solution(numbers):
    ans = [-1]*len(numbers)
    st = []
    
    for i in range(len(numbers)):
        while st and numbers[st[-1]]<numbers[i]:
            idx = st.pop()
            ans[idx]= numbers[i]
        st.append(i)
    return ans