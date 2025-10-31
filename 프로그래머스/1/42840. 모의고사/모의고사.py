def solution(answers):
    st1=  [1,2,3,4,5]
    st2 = [2, 1, 2, 3, 2, 4, 2, 5]
    st3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ans = [0, 0, 0]
    for i in range(len(answers)):
        if st1[i%len(st1)]==answers[i]:
            ans[0]+=1
        if st2[i%len(st2)]==answers[i]:
            ans[1]+=1
        if st3[i%len(st3)]==answers[i]:
            ans[2]+=1
    max_score = max(ans)
    res = []
    for i in range(3):
        if ans[i]==max_score:
            res.append(i+1)
    return res
            