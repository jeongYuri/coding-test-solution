import sys
import bisect
input = sys.stdin.readline

n = int(input())
st = []
total_score = 0
for _ in range(n):
    task = list(map(int,input().split()))
    if task[0]==1:
        score, time = task[1],task[2]
        st.append([score,time])
    if st:
        st[-1][1]-=1 #1분 수행
        if st[-1][1]==0:
            total_score += st[-1][0]
            st.pop()
print(total_score)