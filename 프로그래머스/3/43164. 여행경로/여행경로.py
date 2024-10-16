def solution(tickets):
    answer = []
    arr = dict()
    for start,end in tickets:
        if start in arr:
            arr[start].append(end)
        else:
            arr[start] = [end]
    for i in arr:
        arr[i].sort(reverse = True)
    st = ['ICN']
    while st:
        top = st[-1]
        if (top not in arr)or(not arr[top]):
            answer.append(st.pop())
        else:
            st.append(arr[top].pop())
    return answer[::-1]