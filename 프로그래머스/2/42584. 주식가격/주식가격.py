def solution(prices):
    answer = [0]*len(prices)
    st = []
    for i in range(len(prices)):
        while st and prices[st[-1]]>prices[i]:
            idx = st.pop()
            answer[idx] = i-idx
        st.append(i)
    while st:
        idx = st.pop()
        answer[idx] = len(prices)-1-idx
        
    
    return answer