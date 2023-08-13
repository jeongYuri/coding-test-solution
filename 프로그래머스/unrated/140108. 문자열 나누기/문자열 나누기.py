def solution(s):
    answer = 1
    start = s[0]
    st_cnt = 0
    no_cnt = 0
    for i in s:
        if no_cnt!=0 and st_cnt == no_cnt:
            answer +=1
            no_cnt=0
            st_cnt=0
            start=i
        if i==start:
            st_cnt+=1
        else:
            no_cnt+=1
    return answer