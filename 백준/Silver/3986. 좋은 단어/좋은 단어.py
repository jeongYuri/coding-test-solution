import sys
input = sys.stdin.readline
n = int(input())
cnt = 0
for _ in range(n):
    word = input().strip()
    st = []
    for char in word:
        if st and st[-1]== char:
            st.pop()
        else:
            st.append(char)
    if not st:
        cnt +=1
print(cnt)