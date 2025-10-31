import math
def solution(progresses, speeds):
    st = []
    res = []
    
    days = [math.ceil((100-p)/s) for p,s in zip(progresses, speeds)]
    
    for day in days:
        if not st or day>st[-1][0]:
            st.append([day,1])
        else:
            st[-1][1]+=1
    return [cnt for _, cnt in st]
            