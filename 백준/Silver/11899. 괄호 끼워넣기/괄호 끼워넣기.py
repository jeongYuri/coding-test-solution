import sys
input = sys.stdin.readline


s = input().strip()
st = list(s)
i = 0
while i<len(st)-1:
    if st[i]=='(' and st[i+1]==')':
        st.pop(i)
        st.pop(i)
        if i>0:
            i -=1
    else:
        i+=1
print(len(st))
