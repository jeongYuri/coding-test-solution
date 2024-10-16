from collections import defaultdict

def solution(tickets):
    answer = []
    arr = defaultdict(list)
    for start, end in tickets:
        arr[start].append(end)
    
    for i in arr.keys():
        arr[i].sort()
    
    st = ['ICN'] 
    
    while st:
        q = st[-1]
        
        if arr[q]:  
            st.append(arr[q].pop(0))
        else:
            answer.append(st.pop())
    
    return answer[::-1]